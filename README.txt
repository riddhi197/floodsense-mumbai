FloodSense Mumbai - Dashboard Setup Instructions
====================================================

HOW TO RUN THIS (every time):

1. Unzip this folder somewhere on your laptop (keep all files together)
2. Open Command Prompt / Terminal in that folder
3. First time only: pip install -r requirements.txt
4. Run: streamlit run app.py
5. It opens automatically at http://localhost:8501

IMPORTANT: If you already had an older version running, close it first
(Ctrl+C in its terminal window) before running the new one, and use a
fresh unzip of this folder so old files don't linger.

WHAT'S NEW IN THIS VERSION:

- LIVE RAINFALL (Open-Meteo API): The Flood Prediction tab now pulls
  real-time Mumbai rainfall (today / 3-day / 7-day totals) from the
  free Open-Meteo API - no API key needed. Click "Use Live Data Below"
  to auto-fill the prediction inputs with current conditions. Requires
  an internet connection; refreshes hourly.
- ECONOMIC IMPACT SIMULATOR (new tab): Estimates infrastructure damage
  and business/wage loss (in Rs. Crore) for a chosen flood severity,
  combining each ward's known flood-spot count and population-at-risk
  share. Includes a single-ward view and a citywide view. All
  assumptions are documented in an in-app expander - this is an
  illustrative model, not an official economic forecast.
- CROWDSOURCE HUB (new tab): A working citizen-reporting form (ward,
  location, severity slider, description). Submissions are saved to a
  new `crowd_reports` table in floodsense.db and shown live to anyone
  using the dashboard. Note: on Streamlit Community Cloud, this table
  resets on app restart/redeploy - it's a functional prototype, not
  persistent production storage.
- Historical Explorer explains WHY 2025 data isn't mixed into the
  model (scale mismatch between Konkan and Mumbai City rainfall), and
  shows the actual 2025 Mumbai City rainfall on its own chart instead
- News Analysis tab replaced the decorative word cloud with an actual
  useful severity-scoring chart and table
- About This Project tab explaining the full story and limitations
- Ward drill-down selector
- All EDA and model charts embedded directly in the dashboard

WHAT'S INSIDE THIS FOLDER:
- app.py                              -> run this
- requirements.txt                    -> pip install -r requirements.txt
- floodsense.db                       -> database (now also holds crowd_reports table, created automatically on first run)
- floodsense_final_model.pkl          -> trained model
- mumbai_city_rainfall_2025_clean.csv -> 2025 reference data (not in model)
- nlp_severity_scores.csv / .png      -> NLP severity scoring
- mumbai_ward_risk_map.html           -> interactive map
- remaining .png files                -> EDA / model / clustering charts

TABS IN THE DASHBOARD:
1. About This Project
2. Flood Prediction (now with live Open-Meteo conditions)
3. Historical Explorer (includes 2025 explanation)
4. Ward Risk Map
5. Data Insights (EDA)
6. News Analysis (NLP)
7. Economic Impact Simulator (NEW)
8. Crowdsource Hub (NEW)
