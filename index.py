from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import sqlite3
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

try:
    from api.models_compiled import score_mumbai, score_konkan_final
except ModuleNotFoundError:
    from models_compiled import score_mumbai, score_konkan_final

# Load environment variables for local development
load_dotenv()

app = FastAPI(
    title="FloodSense Mumbai API",
    description="Secure Serverless Backend for Municipal Flood Prediction"
)

# CORS configuration (Compliant with CORS specification)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  # Set to False when using wildcard origins per spec
    allow_methods=["*"],
    allow_headers=["*"],
)

def query_db(query: str):
    """
    Query database with automatic environment check.
    Uses PostgreSQL if DATABASE_URL is set in environment, otherwise falls back to local SQLite.
    NO hardcoded credentials or defaults are used.
    """
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        try:
            conn = psycopg2.connect(database_url)
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return [dict(r) for r in rows]
        except Exception as pg_err:
            print(f"[Database Warning] PostgreSQL connection failed: {pg_err}")
            # Fall through to local SQLite fallback if available

    # Fallback to local SQLite DB if available
    db_path = "floodsense.db"
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            # Auto-populate nlp_news table if missing
            if "nlp_news" in query:
                tables = [r[0] for r in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
                if "nlp_news" not in tables and os.path.exists("nlp_severity_scores.csv"):
                    import pandas as pd
                    df_nlp = pd.read_csv("nlp_severity_scores.csv")
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS nlp_news (
                            Snippet_ID INTEGER PRIMARY KEY,
                            Related_Date TEXT,
                            Severity_Score INTEGER,
                            Keywords_Found TEXT,
                            Snippet_Preview TEXT
                        )
                    """)
                    for _, row in df_nlp.iterrows():
                        cursor.execute(
                            "INSERT OR IGNORE INTO nlp_news VALUES (?, ?, ?, ?, ?)",
                            (int(row['Snippet_ID']), str(row['Related_Date']), int(row['Severity_Score']), str(row['Keywords_Found']), str(row['Snippet_Preview']))
                        )
                    conn.commit()

            cursor.execute(query)
            rows = cursor.fetchall()
            result = [dict(r) for r in rows]
            cursor.close()
            conn.close()
            return result
        except Exception as sq_err:
            raise HTTPException(status_code=500, detail=f"SQLite Database error: {str(sq_err)}")

    raise HTTPException(
        status_code=500,
        detail="Database connection failed: Neither cloud PostgreSQL nor local SQLite database is accessible."
    )

# Request schema for predictions
class PredictRequest(BaseModel):
    scope: str  # "mumbai" or "konkan"
    rain_today: float
    rain_3d: float
    rain_7d: float
    rain_hours: Optional[float] = 4.0
    tide_height_m: Optional[float] = 3.4
    month_val: int

@app.get("/api/health")
def health():
    """
    Real Database Health Ping.
    Executes SELECT 1; against active DB connection.
    """
    db_connected = False
    active_engine = "none"
    
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        try:
            conn = psycopg2.connect(database_url)
            cursor = conn.cursor()
            cursor.execute("SELECT 1;")
            cursor.close()
            conn.close()
            db_connected = True
            active_engine = "postgresql"
        except Exception:
            db_connected = False

    if not db_connected and os.path.exists("floodsense.db"):
        try:
            conn = sqlite3.connect("floodsense.db")
            cursor = conn.cursor()
            cursor.execute("SELECT 1;")
            cursor.close()
            conn.close()
            db_connected = True
            active_engine = "sqlite"
        except Exception:
            db_connected = False

    return {
        "status": "healthy" if db_connected else "degraded",
        "database_connected": db_connected,
        "engine": active_engine
    }

@app.post("/api/predict")
def predict(req: PredictRequest):
    """
    Execute Hydro-Inference Model Prediction.
    Factors in rainfall telemetry, 7-day soil saturation, and Arabian Sea astronomical tide height.
    """
    try:
        tide_boost = 0.0
        if req.tide_height_m and req.tide_height_m >= 4.2:
            tide_boost = 0.25  # High Spring Tide compounding effect
        elif req.tide_height_m and req.tide_height_m >= 3.8:
            tide_boost = 0.12

        if req.scope == "mumbai":
            input_data = [req.rain_today, req.rain_hours or 4.0, req.rain_3d, req.rain_7d]
            # score_mumbai returns [1-p, p] array; extract index [1] safely
            raw_prob = score_mumbai(input_data)[1]
            prob_flood = min(0.98, raw_prob + tide_boost)
        else:
            input_data = [req.rain_today, req.rain_3d, req.rain_7d, req.month_val]
            raw_prob = score_konkan_final(input_data)
            prob_flood = min(0.98, raw_prob + tide_boost)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")

    # Map probability to risk category
    if prob_flood < 0.50:
        category = "No_Flood"
        description = "All systems normal. Weather conditions are within safe historical thresholds."
    elif prob_flood < 0.70:
        category = "Slight"
        description = "Waterlogging expected in chronic low-lying areas. Minor traffic slow-downs."
    elif prob_flood < 0.85:
        category = "Moderate"
        description = "Significant waterlogging in key traffic subway nodes. Local train services may experience delays."
    else:
        category = "Severe"
        description = "Emergency alert! Massive divisional flooding expected. Rivers approaching danger levels. Avoid travel."

    return {
        "scope": req.scope,
        "probability": float(prob_flood),
        "category": category,
        "description": description
    }

@app.get("/api/wards")
def get_wards():
    return query_db("SELECT * FROM ward_risk ORDER BY Ward_Code ASC;")

@app.get("/api/news")
def get_news():
    return query_db("SELECT * FROM nlp_news ORDER BY Related_Date DESC;")

@app.get("/api/historical")
def get_historical():
    return query_db("SELECT Date, Month, Rainfall_mm, Rainfall_3day, Rainfall_7day, Confirmed_Event FROM rainfall_daily ORDER BY Date ASC;")
