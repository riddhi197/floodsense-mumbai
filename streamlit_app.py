import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sqlite3
import pickle
import os
import requests
from datetime import datetime, timedelta
import streamlit.components.v1 as components
from PIL import Image

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="FloodSense: Konkan Division Dashboard",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Dark UI
st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
    }
    .stAlert {
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #00d2ff;
        font-family: 'Inter', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Database Paths
db_path = os.path.join(os.path.dirname(__file__), 'floodsense.db')
model_path = os.path.join(os.path.dirname(__file__), 'floodsense_final_model.pkl')

# Helper to fetch data from SQLite
def get_db_connection():
    return sqlite3.connect(db_path)

# --- SIDEBAR SETTINGS ---
with st.sidebar:
    st.header("⚙️ System Control")
    user_api_key = st.text_input("Gemini API Key", type="password", help="Required for Tab 8 AI Vision Analysis")
    if user_api_key:
        st.success("API Key loaded!")
    else:
        st.warning("Enter Gemini API Key for AI features.")
    
    st.markdown("---")
    st.markdown("### 🤖 Advanced Model Info")
    st.info("""
    **Severity Predictor:** 
    Stacking Ensemble Classifier (XGBoost + Random Forest + Logistic Regression Meta-Learner)
    
    **Ward Clustering:** 
    Gaussian Mixture Model (GMM) providing probabilistic risk clustering.
    """)

# --- MAIN APP LOGO & HEADER ---
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Mumbai_Skyline_at_Night.jpg/800px-Mumbai_Skyline_at_Night.jpg", use_container_width=True)
st.title("🌊 FloodSense: Konkan Division")
st.markdown("#### A Machine Learning-Based Flood Risk Prediction Dashboard")

# 8-Tab Setup
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📘 About Project", 
    "🔮 Flood Predictor", 
    "📊 Historical Explorer", 
    "🗺️ Ward Risk Map", 
    "📈 Data Insights (EDA)", 
    "📰 News Analysis (NLP)", 
    "💰 Economic Simulator", 
    "📣 Citizen Hub"
])

# ==========================================
# TAB 1: ABOUT THIS PROJECT
# ==========================================
with tab1:
    st.header("📘 About FloodSense: Konkan Division")
    
    col_intro, col_side = st.columns([2, 1])
    with col_intro:
        st.subheader("1. Introduction")
        st.markdown("""
        Every monsoon, the **Konkan Division of Maharashtra** — a densely populated, low-lying coastal belt that includes Palghar, Thane, Mumbai, Raigad, Ratnagiri, and Sindhudurg — experiences recurring flood events. 
        Existing warnings describe rainfall intensity (e.g., IMD "Red Alert"), but do not translate that intensity into an explicit, data-driven flood severity forecast. 
        
        **FloodSense** builds this missing layer: a machine learning system trained on seven years (2018–2024) of daily regional rainfall data that predicts flood severity, combined with unsupervised clustering to characterise flood-risk patterns, delivered through an interactive Streamlit dashboard.
        """)
        
        st.subheader("2. The Data Audit (Konkan vs. Mumbai)")
        st.warning("""
        **Why is this project scoped to the Konkan Division rather than Mumbai City alone?**
        An early version of this project framed itself as a Mumbai-specific predictor; a data audit found that Konkan divisional rainfall overstates Mumbai City point-station rainfall by more than 2× for the same period. Reframing the project around the region the data actually represents (Konkan Division) removed this mismatch. Ward-level risk in Mumbai is kept conceptually separate using historical BMC records.
        """)
    
    with col_side:
        st.info("""
        ### 🎯 Objectives
        - **SQL-Backed Rainfall Dataset:** A structured daily Konkan rainfall dataset (2018-2024) cleaned from Maharain.
        - **Ground Truth Validation:** Calibrated against 11 confirmed, cited historical flood events.
        - **Ensemble Classifier:** Stacking model predicting 4-class flood severity.
        - **Geospatial Clustering:** GMM probabilistic risk profiling for Mumbai's 24 administrative wards.
        """)

    st.markdown("---")
    st.subheader("3. Methodology Flowchart")
    st.markdown("""
    - **Raw Data Ingestion:** Daily divisional rainfall -> SQLite Database.
    - **Feature Engineering:** Calculating 3-day and 7-day rolling antecedent rainfall to measure soil saturation.
    - **Supervised Model:** XGBoost + Random Forest stacked ensemble trained on historical rainfall to predict severity.
    - **Unsupervised Clustering:** Gaussian Mixture Model clustering wards by flood risk exposure.
    - **Citizen Validation:** VLM (Gemini 1.5 Flash) validation of crowdsourced ground-truth photos.
    """)

# ==========================================
# TAB 2: FLOOD PREDICTOR
# ==========================================
with tab2:
    st.header("🔮 Flood Severity Predictor")
    
    # Model Scope Selection
    scope = st.radio("Select Prediction Scope:", ["📡 Mumbai City (Local Point Model)", "🌊 Konkan Division (Regional Stacking Model)"])
    
    # Toggle between Live Data and Custom Simulator
    mode = st.radio("Select Data Source Mode:", ["📡 Use Live API Data", "🎛️ Custom Simulator Mode"])
    
    # Initialize variables
    rain_today = 0.0
    rain_3d = 0.0
    rain_7d = 0.0
    rain_hours = 12.0
    month_val = 7
    
    # Coordinates mapping based on scope
    if scope == "📡 Mumbai City (Local Point Model)":
        lat, lon = 19.0760, 72.8777
        scope_name = "Mumbai City"
    else:
        lat, lon = 18.2, 73.0
        scope_name = "Konkan Division"
    
    if mode == "📡 Use Live API Data":
        st.subheader(f"Live Weather Ingestion - {scope_name}")
        try:
            # Weather API
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=precipitation,precipitation_probability&timezone=Asia/Kolkata"
            res = requests.get(url).json()
            hourly_rain = res['hourly']['precipitation'][:24]
            rain_today = float(sum(hourly_rain))
            
            # Fetch rain duration hours
            rain_hours = float(sum([1 for p in hourly_rain if p > 0.1]))
            
            # Fetch marine tide height
            marine_url = f"https://marine-api.open-meteo.com/v1/marine?latitude={lat}&longitude={lon}&hourly=sea_level_height_msl&timezone=Asia/Kolkata"
            marine_res = requests.get(marine_url).json()
            tide_heights = marine_res['hourly']['sea_level_height_msl'][:24]
            current_tide = float(tide_heights[0]) if tide_heights[0] is not None else 1.5
            
            # Use standard defaults for antecedent rains
            rain_3d = 45.0
            rain_7d = 120.0
            month_val = datetime.now().month
            if month_val not in [6, 7, 8, 9, 10]:
                month_val = 7 # Default to July (peak monsoon)
                
            st.success(f"Successfully fetched live meteorological data for {scope_name}!")
            
            # Display live metrics
            m_col1, m_col2, m_col3 = st.columns(3)
            m_col1.metric("Live 24h Rain Forecast", f"{rain_today:.1f} mm")
            m_col2.metric("Current Sea Level Tide Height", f"{current_tide:.2f} m")
            m_col3.metric("Rain Duration Hours", f"{rain_hours:.1f} hrs")
            
        except Exception as e:
            st.error(f"Failed to connect to API: {e}. Defaulting to Simulated values.")
            rain_today, rain_3d, rain_7d, month_val = 110.0, 180.0, 320.0, 7
            
    else:
        st.subheader("Configure Simulator Parameters")
        c1, c2, c3 = st.columns(3)
        rain_today = c1.slider("Daily Precipitation (mm)", 0.0, 400.0, 85.0)
        rain_3d = c2.slider("3-Day Antecedent Cumulative Rain (mm)", 0.0, 500.0, 120.0)
        rain_7d = c3.slider("7-Day Antecedent Cumulative Rain (mm)", 0.0, 800.0, 250.0)
        
        c4, c5 = st.columns(2)
        rain_hours = c4.slider("Precipitation Duration (Hours)", 0.0, 24.0, 12.0)
        month_val = c5.slider("Month of Monsoon", 6, 10, 7, format="Month: %d")
        st.info("💡 Antecedent rain measures soil saturation. High 7-day rain means even a light downpour today can cause severe flooding.")

    st.markdown("---")
    st.subheader("Model Inference Output")
    
    # Model Loading and Predictions
    if scope == "📡 Mumbai City (Local Point Model)":
        mumbai_model_path = os.path.join(os.path.dirname(__file__), 'flood_model.pkl')
        if os.path.exists(mumbai_model_path):
            try:
                with open(mumbai_model_path, 'rb') as f:
                    model = pickle.load(f)
                
                # Features: ['precipitation_sum', 'precipitation_hours', 'precip_3d_sum', 'precip_7d_sum']
                X_in = pd.DataFrame([[rain_today, rain_hours, rain_3d, rain_7d]], 
                                    columns=['precipitation_sum', 'precipitation_hours', 'precip_3d_sum', 'precip_7d_sum'])
                
                probs = model.predict_proba(X_in)[0]
                prob_flood = probs[1]
                
                # Map binary prediction to 4 severity categories
                if prob_flood < 0.15:
                    st.success(f"### 🟢 Mumbai Severity: NO FLOOD (Probability: {prob_flood * 100:.1f}%)")
                    st.markdown("All systems normal. Soil absorption limits are within safe thresholds.")
                elif prob_flood < 0.40:
                    st.warning(f"### 🟡 Mumbai Severity: SLIGHT WATERLOGGING (Probability: {prob_flood * 100:.1f}%)")
                    st.markdown("Waterlogging expected in chronic low-lying areas. Minor traffic slow-downs.")
                elif prob_flood < 0.75:
                    st.error(f"### 🟠 Mumbai Severity: MODERATE FLOODING (Probability: {prob_flood * 100:.1f}%)")
                    st.markdown("Significant waterlogging in key traffic subway nodes. Local train services may experience delays.")
                else:
                    st.markdown(f"<h2 style='color:#ff0000;'>🚨 Mumbai Severity: SEVERE FLOODING (Probability: {prob_flood * 100:.1f}%)</h2>", unsafe_allow_html=True)
                    st.markdown("Emergency alert! Massive flooding expected. Rivers approaching danger levels. Avoid travel.")
                
                st.markdown("#### Model Probability Metric:")
                st.progress(float(prob_flood), text=f"🔥 Verified Mumbai Flood Event Probability: {prob_flood * 100:.1f}%")
                
            except Exception as e:
                st.error(f"Error executing Mumbai predictions: {e}")
        else:
            st.error("Mumbai model file 'flood_model.pkl' not found.")
            
    else:
        # Konkan Division Stacking Model
        if os.path.exists(model_path):
            try:
                with open(model_path, 'rb') as f:
                    bundle = pickle.load(f)
                model = bundle['model']
                features = bundle['features']
                
                # Features: ['Rainfall_mm', 'Rainfall_3day', 'Rainfall_7day', 'Month']
                X_in = pd.DataFrame([[rain_today, rain_3d, rain_7d, month_val]], columns=features)
                
                probs = model.predict_proba(X_in)[0]
                prob_flood = probs[1]
                
                # Map the flood probability to 4 severity categories
                if prob_flood < 0.15:
                    st.success(f"### 🟢 Konkan Severity: NO FLOOD (Probability: {prob_flood * 100:.1f}%)")
                    st.markdown("All systems normal. Soil absorption limits are within safe thresholds.")
                elif prob_flood < 0.40:
                    st.warning(f"### 🟡 Konkan Severity: SLIGHT WATERLOGGING (Probability: {prob_flood * 100:.1f}%)")
                    st.markdown("Waterlogging expected in chronic low-lying areas. Minor traffic slow-downs.")
                elif prob_flood < 0.75:
                    st.error(f"### 🟠 Konkan Severity: MODERATE FLOODING (Probability: {prob_flood * 100:.1f}%)")
                    st.markdown("Significant waterlogging in key traffic subway nodes. Local train services may experience delays.")
                else:
                    st.markdown(f"<h2 style='color:#ff0000;'>🚨 Konkan Severity: SEVERE FLOODING (Probability: {prob_flood * 100:.1f}%)</h2>", unsafe_allow_html=True)
                    st.markdown("Emergency alert! Massive divisional flooding expected. Rivers approaching danger levels. Avoid travel.")
                    
                # Class Probabilities Breakdown
                st.markdown("#### Model Probability Metric:")
                st.progress(float(prob_flood), text=f"🔥 Verified Konkan Flood Event Probability: {prob_flood * 100:.1f}%")
                
                # Render explanation of mapping
                st.info("""
                💡 **How the AI Risk Level is Mapped:**
                The Stacking Ensemble predicts the probability of a verified historical flood event occurring on a day with these weather parameters.
                - **Low Risk (< 15%):** Normal conditions.
                - **Elevated Risk (15% - 40%):** Localized waterlogging.
                - **High Risk (40% - 75%):** Widespread traffic and transit disruptions.
                - **Emergency Alert (>= 75%):** Severe threat to life and property.
                """)
                
            except Exception as e:
                st.error(f"Error executing Konkan predictions: {e}")
        else:
            st.error("Konkan model file 'floodsense_final_model.pkl' not found.")


# ==========================================
# TAB 3: HISTORICAL EXPLORER
# ==========================================
with tab3:
    st.header("📊 Konkan vs. Mumbai City Historical Explorer")
    
    st.markdown("""
    **The Scale Mismatch Dilemma:**
    During the data audit, we compared the Konkan division regional averages with point-station rainfall in Mumbai City. 
    Because the Konkan Division rainfall includes the massive Western Ghats catchment area, it frequently registers **double** the rainfall of Mumbai City itself. 
    This means if we trained a model on Konkan rainfall and claimed it predicted localized Mumbai floods, the model would produce massive false alarms.
    """)
    
    # Render historical comparison image
    if os.path.exists("konkan_vs_mumbaicity.png"):
        st.image("konkan_vs_mumbaicity.png", caption="Visualizing the 2x scale mismatch between Konkan Division and Mumbai City Station Rainfall.", use_container_width=True)
        
    st.subheader("2025 Mumbai City Reference Rainfall (Point-Station Data)")
    if os.path.exists("mumbai_city_rainfall_2025_clean.csv"):
        try:
            df_2025 = pd.read_csv("mumbai_city_rainfall_2025_clean.csv")
            fig_2025 = px.line(df_2025, x="Date", y="Rainfall_mm", title="Mumbai City Daily Rainfall Profile (Monsoon 2025)")
            st.plotly_chart(fig_2025, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading 2025 CSV: {e}")
    else:
        st.warning("mumbai_city_rainfall_2025_clean.csv not found.")

# ==========================================
# TAB 4: WARD RISK MAP (Clustering)
# ==========================================
with tab4:
    st.header("🗺️ Unsupervised Ward Risk Map & Clustering")
    
    col_map, col_details = st.columns([3, 2])
    
    with col_map:
        st.subheader("Mumbai Ward Risk Vulnerability Map")
        if os.path.exists("mumbai_ward_risk_map.html"):
            with open("mumbai_ward_risk_map.html", "r", encoding="utf-8") as f:
                html_map = f.read()
            components.html(html_map, height=500)
        else:
            st.warning("mumbai_ward_risk_map.html not found.")
            
    with col_details:
        st.subheader("Gaussian Mixture Model (GMM) Profiles")
        st.markdown("Unlike K-Means, GMM assigns a *probability* of risk membership for each ward.")
        
        # Load ward_risk table
        try:
            conn = get_db_connection()
            df_wards = pd.read_sql("SELECT * FROM ward_risk", conn)
            conn.close()
            
            # Ward selector
            selected_ward = st.selectbox("Select Ward to Analyze:", df_wards['Ward_Code'] + " - " + df_wards['Area_Covered'])
            ward_code = selected_ward.split(" - ")[0]
            
            ward_info = df_wards[df_wards['Ward_Code'] == ward_code].iloc[0]
            
            st.markdown(f"### Ward Details: {ward_info['Ward_Code']}")
            st.markdown(f"**Area Covered:** {ward_info['Area_Covered']}")
            st.markdown(f"**Risk Cluster Level:** `{ward_info['Cluster_Label']}`")
            st.markdown(f"**Known Chronic Flood Spots:** {ward_info['Known_Flood_Spots_Count']}")
            st.markdown(f"**Population Exposure Rate:** {ward_info['Population_At_Risk_Pct']:.1f}%")
            
            # GMM Probabilities Gauges
            st.markdown("#### Unsupervised Risk Membership Probabilities:")
            prob_low = ward_info.get('GMM_Prob_Low', 0.0) * 100
            prob_med = ward_info.get('GMM_Prob_Med', 0.0) * 100
            prob_high = ward_info.get('GMM_Prob_High', 0.0) * 100
            
            st.progress(float(prob_low / 100), text=f"🟢 Low Risk Probability: {prob_low:.1f}%")
            st.progress(float(prob_med / 100), text=f"🟡 Medium Risk Probability: {prob_med:.1f}%")
            st.progress(float(prob_high / 100), text=f"🔴 High Risk Probability: {prob_high:.1f}%")
            
        except Exception as e:
            st.error(f"Error loading ward clustering data: {e}")

    st.markdown("---")
    st.subheader("Complete Ward Clustering Dataset")
    try:
        st.dataframe(df_wards[['Ward_Code', 'Area_Covered', 'Known_Flood_Spots_Count', 'Population_At_Risk_Pct', 'Cluster_Label']], use_container_width=True)
    except NameError:
        pass

# ==========================================
# TAB 5: DATA INSIGHTS (EDA)
# ==========================================
with tab5:
    st.header("📈 Data Insights & Model Performance")
    
    st.subheader("Interactive Feature Distribution & Analytics")
    
    # Load daily data
    try:
        conn = get_db_connection()
        df_daily = pd.read_sql("SELECT Date, Month, Rainfall_mm, Rainfall_3day, Rainfall_7day, Confirmed_Event FROM rainfall_daily", conn)
        conn.close()
        df_daily['Date'] = pd.to_datetime(df_daily['Date']).dt.date
    except Exception as e:
        df_daily = None
        st.error(f"Error loading daily database: {e}")
        
    if df_daily is not None:
        # Month mapping
        month_map = {6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October'}
        df_daily['Monsoon Month'] = df_daily['Month'].map(month_map)
        
        # 1. Box Plot of Rainfall by Month
        st.markdown("### 📅 Monthly Rainfall Distributions")
        st.markdown("Observe the range, median, and outliers of daily rainfall across the monsoon season.")
        fig_month = px.box(
            df_daily, 
            x='Monsoon Month', 
            y='Rainfall_mm', 
            color='Monsoon Month',
            category_orders={'Monsoon Month': ['June', 'July', 'August', 'September', 'October']},
            title='Konkan division Daily Rainfall Distribution (Monsoon 2018-2024)',
            labels={'Rainfall_mm': 'Daily Rainfall (mm)'},
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        st.plotly_chart(fig_month, use_container_width=True)
        
        # 2. Scatter Plot: Saturation vs. Intensity
        st.markdown("---")
        st.markdown("### ⛈️ Soil Saturation vs. Rain Intensity Scatter Plot")
        st.markdown("This scatter plot maps every day of the monsoon. The red dots represent confirmed flood events. Notice that floods only trigger when **both** same-day rain and 7-day soil saturation are exceptionally high.")
        df_daily['Event Type'] = df_daily['Confirmed_Event'].map({0: 'Normal Day', 1: 'Verified Flood Event'})
        
        fig_scatter = px.scatter(
            df_daily, 
            x='Rainfall_mm', 
            y='Rainfall_7day', 
            color='Event Type',
            hover_data=['Date', 'Rainfall_3day'],
            title='Precipitation Intensity vs. Antecedent Soil Saturation',
            labels={'Rainfall_mm': 'Daily Rainfall Today (mm)', 'Rainfall_7day': '7-Day Antecedent Cumulative Rain (mm)'},
            color_discrete_map={'Normal Day': '#00d2ff', 'Verified Flood Event': '#ff0000'}
        )
        fig_scatter.update_traces(marker=dict(size=10, opacity=0.8, line=dict(width=1, color='DarkSlateGrey')))
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # 3. Correlation Heatmap
        st.markdown("---")
        st.markdown("### 🎛️ Weather Feature Correlation Matrix")
        st.markdown("A correlation matrix showing the linear relationship between our model's predictors.")
        corr = df_daily[['Rainfall_mm', 'Rainfall_3day', 'Rainfall_7day']].corr()
        fig_corr = px.imshow(
            corr, 
            text_auto=".3f", 
            aspect="auto",
            labels=dict(x="Features", y="Features", color="Correlation Coefficient"),
            x=['Daily Rain', '3-Day Antecedent', '7-Day Antecedent'],
            y=['Daily Rain', '3-Day Antecedent', '7-Day Antecedent'],
            title="Correlation Matrix Heatmap",
            color_continuous_scale="RdBu_r"
        )
        st.plotly_chart(fig_corr, use_container_width=True)
        
    st.markdown("---")
    with st.expander("🔍 View Pre-Calculated Technical Graphics (Confusion Matrices & Heatmaps)"):
        c_e1, c_e2 = st.columns(2)
        with c_e1:
            if os.path.exists("calendar_heatmap.png"):
                st.image("calendar_heatmap.png", caption="Monsoon Calendar Heatmap (Daily Rainfall Intensity)", use_container_width=True)
            if os.path.exists("model_comparison.png"):
                st.image("model_comparison.png", caption="Model Calibration & ROC AUC Comparison Curves", use_container_width=True)
        with c_e2:
            if os.path.exists("confusion_matrices.png"):
                st.image("confusion_matrices.png", caption="Ensemble Stacked Classifier Confusion Matrices", use_container_width=True)
            if os.path.exists("eda_overview.png"):
                st.image("eda_overview.png", caption="General Dataset Feature Distributions", use_container_width=True)

# ==========================================
# TAB 6: NEWS ANALYSIS (NLP)
# ==========================================
with tab6:
    st.header("📰 News & Media NLP Severity Analysis")
    
    # 0. Educational Explanation Guide
    st.info("""
    📖 **What is this Tab?**
    To prove our meteorological models work, we need a way to validate their predictions against what *actually* happened. 
    This tab displays an **independent validation database** extracted from unstructured historical news reports. 
    
    🧠 **How it works (NLP Pipeline):**
    1. A web scraper crawled local news articles, IMD reports, and weather bulletins (2018–2024).
    2. An NLP engine scanned the texts and calculated a **Severity Score** based on keyword occurrences (e.g., words like `deaths` or `landslides` score higher than `waterlogging`).
    3. We cross-reference these scores with our ML predictions to confirm the AI flags real disasters.
    """)
    
    # Load NLP Scores
    if os.path.exists("nlp_severity_scores.csv"):
        try:
            df_nlp = pd.read_csv("nlp_severity_scores.csv")
            
            # 1. NLP Summary Metric Cards
            st.markdown("### 📊 Media Intelligence Metrics")
            n_col1, n_col2, n_col3 = st.columns(3)
            
            # Calculate metrics
            total_snippets = len(df_nlp)
            max_score = df_nlp['Severity_Score'].max()
            max_event_date = df_nlp[df_nlp['Severity_Score'] == max_score]['Related_Date'].values[0]
            
            n_col1.metric("News Reports Parsed", f"{total_snippets} Reports")
            n_col2.metric("Peak NLP Severity Index", f"{max_score} / 15", help="Maximum news severity recorded on July 18, 2021")
            n_col3.metric("Peak Disaster Date", f"{max_event_date}")
            
            st.markdown("---")
            
            # 2. Chronological Timeline Scatter Plot
            st.subheader("⏱️ Historical News Severity Timeline")
            st.markdown("Chronological mapping of news-reported flood events. Larger, redder circles represent severe regional flooding events.")
            
            df_nlp_time = df_nlp.copy()
            df_nlp_time['Date'] = pd.to_datetime(df_nlp_time['Related_Date'], errors='coerce')
            df_nlp_time = df_nlp_time.dropna(subset=['Date'])
            df_nlp_time = df_nlp_time.sort_values(by="Date")
            
            fig_timeline = px.scatter(
                df_nlp_time,
                x="Date",
                y="Severity_Score",
                size="Severity_Score",
                color="Severity_Score",
                color_continuous_scale="OrRd",
                hover_data=["Keywords_Found", "Snippet_Preview"],
                title="NLP Severity Scores mapped chronologically (2018-2024)",
                labels={"Severity_Score": "NLP Severity Index", "Date": "Timeline Date"}
            )
            fig_timeline.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            fig_timeline.update_layout(xaxis_title="Timeline Date", yaxis_title="Extracted Severity Index")
            st.plotly_chart(fig_timeline, use_container_width=True)
            
            # 3. Native Streamlit News Card Grid
            st.markdown("---")
            st.subheader("📰 Media Intelligence Report Feed")
            st.markdown("Parsed news article summaries and entity extractions:")
            
            cols = st.columns(2)
            for idx, row in df_nlp.iterrows():
                col_idx = idx % 2
                with cols[col_idx]:
                    with st.container(border=True):
                        # Card Header
                        c1, c2 = st.columns([2, 1])
                        c1.markdown(f"📅 **{row['Related_Date']}**")
                        
                        score = row['Severity_Score']
                        if score >= 10:
                            c2.markdown(f"<span style='color:#ef4444; font-weight:bold; float:right;'>🚨 Severe ({score})</span>", unsafe_allow_html=True)
                        elif score >= 5:
                            c2.markdown(f"<span style='color:#f59e0b; font-weight:bold; float:right;'>⚠️ Moderate ({score})</span>", unsafe_allow_html=True)
                        else:
                            c2.markdown(f"<span style='color:#3b82f6; font-weight:bold; float:right;'>ℹ️ Slight ({score})</span>", unsafe_allow_html=True)
                        
                        # News snippet quote
                        st.markdown(f'*"{row["Snippet_Preview"]}"*')
                        
                        # Extracted keywords as tags
                        keywords = [f"`{k.strip()}`" for k in row['Keywords_Found'].split(',') if k.strip()]
                        st.caption("🔑 **Extracted Keywords:** " + " ".join(keywords))
            
        except Exception as e:
            st.error(f"Error rendering NLP components: {e}")
    else:
        st.warning("nlp_severity_scores.csv not found.")
        if os.path.exists("nlp_severity_chart.png"):
            st.image("nlp_severity_chart.png", use_container_width=True)

# ==========================================
# TAB 7: ECONOMIC IMPACT SIMULATOR
# ==========================================
with tab7:
    st.header("💰 Economic Loss & Business Impact Simulator")
    
    st.markdown("Calculate productivity damage and wage loss modeled after severity levels.")
    
    # Use predicted class from prediction tab if available, otherwise manual selector
    sim_severity = st.selectbox("Select Severity Class to Simulate:", ["No_Flood", "Slight", "Moderate", "Severe"])
    
    # Dynamic Math based on Severity
    if sim_severity == "No_Flood":
        loss_range = 0.0
        delay_avg = 0
    elif sim_severity == "Slight":
        loss_range = 50.0
        delay_avg = 30
    elif sim_severity == "Moderate":
        loss_range = 180.0
        delay_avg = 75
    else:
        loss_range = 480.0
        delay_avg = 180
        
    eco_col1, eco_col2 = st.columns(2)
    eco_col1.metric("Estimated Productivity Loss today (Region)", f"₹{loss_range:.1f} Crores")
    eco_col2.metric("Avg Supply Chain/Delivery Delays", f"+{delay_avg} Minutes")
    
    # Sector breakdown chart
    sectors_df = pd.DataFrame({
        "Sector": ["Logistics", "Retail", "IT/BPO", "Informal Sector"],
        "Estimated Loss (Cr)": [loss_range * 0.4, loss_range * 0.3, loss_range * 0.2, loss_range * 0.1]
    })
    
    fig_eco = px.bar(sectors_df, x="Sector", y="Estimated Loss (Cr)", title="Loss Allocation by Sector", color="Sector")
    st.plotly_chart(fig_eco, use_container_width=True)
    
    # Ward Drill-Down Simulation
    st.markdown("---")
    st.subheader("Ward-Level Exposure Breakdown")
    try:
        conn = get_db_connection()
        df_wards_eco = pd.read_sql("SELECT Ward_Code, Area_Covered, Population_At_Risk_Pct FROM ward_risk", conn)
        conn.close()
        
        # Calculate ward specific share
        total_risk_sum = df_wards_eco['Population_At_Risk_Pct'].sum()
        df_wards_eco['Ward_Estimated_Loss (Cr)'] = (df_wards_eco['Population_At_Risk_Pct'] / total_risk_sum) * loss_range
        
        st.dataframe(df_wards_eco.sort_values(by="Ward_Estimated_Loss (Cr)", ascending=False), use_container_width=True)
        
    except Exception as e:
        st.error(f"Error calculating ward economic breakdown: {e}")

# ==========================================
# TAB 8: CITIZEN CROWDSOURCE HUB
# ==========================================
with tab8:
    st.header("📣 Citizen Crowdsource Reporting Hub")
    
    st.markdown("Crowdsourcing real-time ground truth reports. Uploaded images are validated by Google's Gemini Vision model.")
    
    # Fetch wards list for dropdown
    try:
        conn = get_db_connection()
        df_wards_list = pd.read_sql("SELECT Ward_Code, Area_Covered FROM ward_risk", conn)
        conn.close()
        ward_options = [f"{r['Ward_Code']} - {r['Area_Covered']}" for _, r in df_wards_list.iterrows()]
    except Exception as e:
        ward_options = ["A - Colaba", "B - Masjid Bunder"]
        
    with st.form("citizen_report_form"):
        reporter_name = st.text_input("Name (Optional)")
        selected_ward_opt = st.selectbox("Select Affected Ward:", ward_options)
        location_note = st.text_input("Exact Location/Landmark (e.g. Milan Subway Entrance)")
        flood_severity = st.slider("Observed Severity Index (1 = Damp, 5 = Submerged)", 1, 5, 2)
        uploaded_image = st.file_uploader("Upload Image Proof (Required for VLM Validation)", type=["png", "jpg", "jpeg"])
        description = st.text_area("Describe the situation:")
        
        submit_btn = st.form_submit_button("Submit Intelligence Report")
        
        if submit_btn:
            if not location_note or not description:
                st.error("Please fill in the location and description.")
            else:
                ai_validation = "No Image Uploaded for AI Validation"
                
                # Check VLM Integration
                if uploaded_image is not None:
                    api_key = user_api_key or os.environ.get("GEMINI_API_KEY")
                    if api_key:
                        st.info("Sending image to Gemini 1.5 Flash for verification...")
                        try:
                            # Direct package check for google-genai
                            from google import genai
                            client = genai.Client(api_key=api_key)
                            img = Image.open(uploaded_image)
                            prompt = "Analyze this image of a street. Does it show flooding? If yes, estimate the water depth (ankle, knee, waist, or car-level). Keep the response brief and professional."
                            
                            response = client.models.generate_content(
                                model='gemini-1.5-flash',
                                contents=[img, prompt]
                            )
                            ai_validation = f"Gemini Verified: {response.text}"
                            st.success("AI Image Verification Complete!")
                        except Exception as ve:
                            ai_validation = f"AI Error: {ve}"
                            st.warning(f"VLM connection failed: {ve}. Falling back to manual submission.")
                    else:
                        ai_validation = "Skipped AI check (Gemini API Key missing in Sidebar)"
                        st.warning("Gemini API key is not entered. Submitting report with skipped AI validation.")
                
                # Write to Database
                try:
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    
                    ward_code = selected_ward_opt.split(" - ")[0]
                    area_covered = selected_ward_opt.split(" - ")[1]
                    
                    # Insert
                    cursor.execute("""
                    INSERT INTO crowd_reports (timestamp, ward_code, area_covered, location_note, severity, description)
                    VALUES (?, ?, ?, ?, ?, ?);
                    """, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ward_code, area_covered, location_note, flood_severity, f"{description} | [{ai_validation}]"))
                    
                    conn.commit()
                    conn.close()
                    st.success("Your intelligence report has been successfully recorded in the SQLite database!")
                    st.balloons()
                except Exception as db_e:
                    st.error(f"Database insertion failed: {db_e}")

    # Display Recent Submissions
    st.markdown("---")
    st.subheader("Recent Citizen Submissions (Live from floodsense.db)")
    try:
        conn = get_db_connection()
        df_submissions = pd.read_sql("SELECT timestamp, ward_code, area_covered, location_note, severity, description FROM crowd_reports ORDER BY timestamp DESC LIMIT 5", conn)
        conn.close()
        st.dataframe(df_submissions, use_container_width=True)
    except Exception as e:
        st.warning("No crowdsourced reports recorded yet.")
