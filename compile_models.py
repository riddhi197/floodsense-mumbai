import pickle
import os
import m2cgen as m2c

base_dir = r"C:\Users\User\.gemini\antigravity\scratch\floodsense_mumbai"

# 1. Load Mumbai Model (XGBoost)
mumbai_path = os.path.join(base_dir, 'flood_model.pkl')
with open(mumbai_path, 'rb') as f:
    mumbai_model = pickle.load(f)

# Fix for m2cgen + XGBoost 2.0+ base_score None bug
mumbai_model.base_score = 0.5

print("Compiling Mumbai Model...")
mumbai_code = m2c.export_to_python(mumbai_model)
# Rename the main function
mumbai_code = mumbai_code.replace("def score(input):", "def score_mumbai(input):")

# 2. Load Konkan Model (Stacking)
konkan_path = os.path.join(base_dir, 'floodsense_final_model.pkl')
with open(konkan_path, 'rb') as f:
    konkan_bundle = pickle.load(f)

stack_model = konkan_bundle['model']
rf_est = stack_model.estimators_[0]
xgb_est = stack_model.estimators_[1]
lr_meta = stack_model.final_estimator_

# Fix for m2cgen + XGBoost 2.0+ base_score None bug
xgb_est.base_score = 0.5

print("Compiling Konkan Base RF Estimator...")
rf_code = m2c.export_to_python(rf_est)
rf_code = rf_code.replace("def score(input):", "def score_konkan_rf(input):")

print("Compiling Konkan Base XGB Estimator...")
xgb_code = m2c.export_to_python(xgb_est)
xgb_code = xgb_code.replace("def score(input):", "def score_konkan_xgb(input):")

# Get Logistic Regression metadata
coef = lr_meta.coef_[0]
intercept = lr_meta.intercept_[0]
print(f"Logistic Regression Meta: Coef={coef}, Intercept={intercept}")

# 3. Write compiled model code to api/models_compiled.py
output_path = os.path.join(base_dir, 'api', 'models_compiled.py')

compiled_file_content = f"""# Auto-generated pure-Python model predictions (zero dependencies)
import math

# --- Mumbai Model: XGBoost ---
# Input: [precipitation_sum, precipitation_hours, precip_3d_sum, precip_7d_sum]
{mumbai_code}

# --- Konkan Base 1: Random Forest ---
# Input: [Rainfall_mm, Rainfall_3day, Rainfall_7day, Month]
{rf_code}

# --- Konkan Base 2: XGBoost ---
# Input: [Rainfall_mm, Rainfall_3day, Rainfall_7day, Month]
{xgb_code}

# --- Logistic Regression Meta-Classifier for Stacking ---
COEF_RF = {coef[0]}
COEF_XGB = {coef[1]}
INTERCEPT = {intercept}

def score_konkan_final(input_array):
    p_rf = score_konkan_rf(input_array)
    p_xgb = score_konkan_xgb(input_array)
    
    # Stacking combining logic (meta-classifier Logistic Regression)
    z = (COEF_RF * p_rf) + (COEF_XGB * p_xgb) + INTERCEPT
    # Sigmoid function
    return 1.0 / (1.0 + math.exp(-z))
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(compiled_file_content)

print(f"Successfully generated pure Python model code at: {output_path}")
