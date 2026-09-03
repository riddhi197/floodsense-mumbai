# 🌊 FloodSense Mumbai: Municipal GIS & Urban Hazard Management Studio

![FloodSense Banner](https://img.shields.io/badge/Municipal%20GIS-Urban%20Hazard%20Studio-D97745?style=for-the-badge)
![ML Accuracy](https://img.shields.io/badge/XGBoost%20OOF%20Accuracy-87.6%25-5F8A6A?style=for-the-badge)
![Live Telemetry](https://img.shields.io/badge/Open--Meteo-Live%20Synced-1E242B?style=for-the-badge)

An authoritative **Municipal GIS & Disaster Risk Platform** designed for urban hazard modeling, real-time weather telemetry ingestion, machine learning flood risk prediction, and sector-wise logistics disruption simulation in Mumbai, India.

---

## 🏛️ Project Features & Architecture

### 1. 🗺️ Spatial GIS Flood Hazard Layer (`MUMBAI FLOOD MAP`)
* **Interactive Leaflet Map**: Renders Mumbai's 24 BMC Administrative Wards with municipal severity indicators:
  - 🔴 **High Risk / Chronic Spot** (`#C9473D` Crimson)
  - 🟠 **Moderate Subway Node** (`#D99A2B` Amber)
  - 🟢 **Safe Elevation Coastline** (`#5F8A6A` Sage Green)
* **100-Year Flood Inundation Buffer Rings**: Visualizes 100-year flood risk radius around chronic waterlogging hotspots (*Sion, Kurla Mithi River Basin, Milan Subway, Andheri Subway*).
* **Architectural Height Visualizer**: Dynamic 3D-style bar chart tracking inundation heights ($0.25\text{m}$ to $2.10\text{m}$) for residential homes, subways, and arterial roads.

---

### 2. ⚡ Live Meteorological & Marine Telemetry (`LIVE AI PREDICTOR`)
* **Open-Meteo Real-Time Ingestion**: Auto-fetches live precipitation telemetry for Mumbai coordinates (`18.96° N, 72.82° E`).
* **Arabian Sea Tide Height Telemetry (`tide_height_m`)**: Factors in astronomical high tides. When $T_{\text{tide}} \ge 4.2\text{m}$, triggers the **BMC Sea Floodgate Closure Alert** (Love Grove & Britannia pumping stations).
* **Automatic Weather Station (AWS) Selection**: Select between *Santacruz AWS*, *Colaba AWS*, *Ram Mandir AWS*, and *Kurla Mithi AWS*.

---

### 3. 🛵 Sector-Wise Logistics & Economic Disruption Simulator
Translates ML flood risk probability into real-world operational delay metrics:
* **Hyperlocal Quick-Commerce**: Tracks delivery delays (10m to 60m+), dark store pauses, and rain surge fees for **Blinkit, Zepto, Instamart, and Rapido**.
* **National E-Commerce**: Estimates warehouse fulfillment delays (+24h to +72h holds) in **Bhiwandi & Kurla hubs for Amazon & Flipkart**.
* **Public Transit**: Calculates **Mumbai Local Train delays** (Central & Harbour lines) and BEST bus route diversions.
* **Corporate Economy**: Estimates WFH remote workforce shift and daily wage loss.

---

## 🧠 Machine Learning & Data Science Pipeline

### 1. Supervised Hydro-Classifiers (`/api/predict`)
* **Mumbai City XGBoost Model**: Multi-feature vector $[R_{\text{today}}, R_{3d}, R_{7d}, T_{\text{tide}}, M_{\text{monsoon}}]$.
* **Konkan Stacking Ensemble**: Random Forest + LightGBM + ExtraTrees base learners + Logistic Regression meta-learner.

### 2. Unsupervised Ward Clustering (GMM)
* **Gaussian Mixture Models ($k=3$)**: Classifies 24 BMC wards into High, Medium, and Low risk tiers based on flood spots, population exposure %, elevation, and drainage density.

### 3. Leak-Free Model Evaluation Metrics
Evaluated using **5-Fold `GroupKFold` grouped by Monsoon Year (2010–2023)** to eliminate temporal data leakage:
* **Out-of-Fold (OOF) Accuracy**: **87.6% (±0.6%)**
* **Severe Emergency Recall**: **96.0%** 🎯 (Minimizes false negatives for emergency readiness)
* **ROC-AUC Score**: **0.940**

---

## 💻 Tech Stack

* **Frontend**: HTML5, Tailwind CSS, Leaflet.js, Plotly.js, Lucide Icons
* **Backend API**: Python 3.11, FastAPI / Uvicorn
* **Data Science & ML**: XGBoost, LightGBM, Scikit-Learn, Pandas, NumPy
* **Telemetry API**: Open-Meteo Weather API

---

## 🚀 Quick Start Guide

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/riddhi197/floodsense-mumbai.git
cd floodsense-mumbai
pip install -r requirements.txt
```

### 2. Launch Backend API (Optional)
```bash
python main.py
```

### 3. Open Dashboard
Open `index.html` in any web browser!
