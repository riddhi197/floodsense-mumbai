from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Load env variables for local dev
load_dotenv()

app = FastAPI(title="FloodSense Mumbai API", description="Serverless backend for Vercel")

# Enable CORS for Next.js frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fetch Database URL from Environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres.ddgemcedpteukdntyqii:9028049003%40shetye@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres")

def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

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
    return {"status": "healthy", "database_connected": True}

@app.post("/api/predict")
def predict(req: PredictRequest):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    if req.scope == "mumbai":
        model_path = os.path.join(base_dir, 'flood_model.pkl')
        if not os.path.exists(model_path):
            raise HTTPException(status_code=404, detail="Mumbai flood model not found.")
            
        try:
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
                
            X_in = pd.DataFrame(
                [[req.rain_today, req.rain_hours, req.rain_3d, req.rain_7d]], 
                columns=['precipitation_sum', 'precipitation_hours', 'precip_3d_sum', 'precip_7d_sum']
            )
            probs = model.predict_proba(X_in)[0]
            prob_flood = float(probs[1])
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")
            
    else:
        model_path = os.path.join(base_dir, 'floodsense_final_model.pkl')
        if not os.path.exists(model_path):
            raise HTTPException(status_code=404, detail="Konkan regional model not found.")
            
        try:
            with open(model_path, 'rb') as f:
                bundle = pickle.load(f)
            model = bundle['model']
            features = bundle['features']
            
            X_in = pd.DataFrame([[req.rain_today, req.rain_3d, req.rain_7d, req.month_val]], columns=features)
            probs = model.predict_proba(X_in)[0]
            prob_flood = float(probs[1])
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")
            
    # Map probability to risk category
    if prob_flood < 0.15:
        category = "No_Flood"
        description = "All systems normal. Soil absorption limits are within safe thresholds."
    elif prob_flood < 0.40:
        category = "Slight"
        description = "Waterlogging expected in chronic low-lying areas. Minor traffic slow-downs."
    elif prob_flood < 0.75:
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
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT * FROM ward_risk ORDER BY Ward_Code ASC;")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/api/news")
def get_news():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT * FROM nlp_news ORDER BY Related_Date DESC;")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@app.get("/api/historical")
def get_historical():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT Date, Month, Rainfall_mm, Rainfall_3day, Rainfall_7day, Confirmed_Event FROM rainfall_daily ORDER BY Date ASC;")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
