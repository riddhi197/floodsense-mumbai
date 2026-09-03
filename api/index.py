from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
try:
    from api.models_compiled import score_mumbai, score_konkan_final
except ModuleNotFoundError:
    from models_compiled import score_mumbai, score_konkan_final

# Load env variables for local dev
load_dotenv()

app = FastAPI(title="FloodSense Mumbai API", description="Serverless backend for Vercel")

# Enable CORS for Next.js frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to Vercel domain
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

import sqlite3

# Fetch Database URL from Environment
DATABASE_URL = os.getenv("DATABASE_URL")

def query_db(query: str):
    # Try PostgreSQL first if DATABASE_URL is set
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
        except Exception:
            pass

    # Fallback to local SQLite DB if available
    db_path = "floodsense.db"
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            # If nlp_news table is missing in SQLite, auto-populate from nlp_severity_scores.csv
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
            raise HTTPException(status_code=500, detail=f"Database query error: {str(sq_err)}")

    raise HTTPException(status_code=500, detail="Database connection error: Neither cloud PostgreSQL nor local SQLite database is accessible.")

# Request schema for predictions
class PredictRequest(BaseModel):
    scope: str # "mumbai" or "konkan"
    rain_today: float
    rain_3d: float
    rain_7d: float
    rain_hours: float
    month_val: int

@app.get("/api/health")
def health():
    db_connected = False
    try:
        query_db("SELECT 1;")
        db_connected = True
    except Exception:
        db_connected = False
        
    return {
        "status": "healthy" if db_connected else "degraded",
        "database_connected": db_connected
    }

@app.post("/api/predict")
def predict(req: PredictRequest):
    try:
        if req.scope == "mumbai":
            # Input features: ['precipitation_sum', 'precipitation_hours', 'precip_3d_sum', 'precip_7d_sum']
            input_data = [req.rain_today, req.rain_hours, req.rain_3d, req.rain_7d]
            prob_flood = score_mumbai(input_data)[1]
        else:
            # Input features: ['Rainfall_mm', 'Rainfall_3day', 'Rainfall_7day', 'Month']
            input_data = [req.rain_today, req.rain_3d, req.rain_7d, req.month_val]
            prob_flood = score_konkan_final(input_data)
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")

    # Map probability to risk category (Tuned for high precision to avoid false alarms in portfolio demo)
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
        "probability": prob_flood,
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

