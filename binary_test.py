import pandas as pd
import numpy as np
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, recall_score

db_path = 'C:/Users/User/Downloads/FloodSense_Mumbai/FloodSense_Mumbai/floodsense.db'
conn = sqlite3.connect(db_path)
df = pd.read_sql('SELECT * FROM rainfall_daily', conn)
conn.close()

# Features
features = ['Rainfall_mm', 'Rainfall_3day', 'Rainfall_7day', 'Month']
X = df[features]

# Target: Real Ground-Truth Confirmed Flood Events (Binary)
y = df['Confirmed_Event']

print("Total days:", len(y))
print("Confirmed flood days:", sum(y))

# Train/Test split (stratified because of massive imbalance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Use scale_pos_weight in XGBoost to handle class imbalance
num_neg = sum(y_train == 0)
num_pos = sum(y_train == 1)
scale_weight = num_neg / max(num_pos, 1)

base_estimators = [
    ('rf', RandomForestClassifier(n_estimators=50, max_depth=3, class_weight='balanced', random_state=42)),
    ('xgb', XGBClassifier(n_estimators=50, max_depth=3, scale_pos_weight=scale_weight, random_state=42, eval_metric='logloss'))
]

meta_learner = LogisticRegression(random_state=42)

stack_model = StackingClassifier(
    estimators=base_estimators,
    final_estimator=meta_learner,
    cv=5,
    n_jobs=-1
)

stack_model.fit(X_train, y_train)

# Predictions
y_pred_train = stack_model.predict(X_train)
y_pred_test = stack_model.predict(X_test)

print("\n--- Training Set Metrics ---")
print("Accuracy:", accuracy_score(y_train, y_pred_train))
print("Recall on Floods:", recall_score(y_train, y_pred_train))

print("\n--- Unseen Test Set Metrics ---")
print("Accuracy:", accuracy_score(y_test, y_pred_test))
print("Recall on Floods:", recall_score(y_test, y_pred_test))
print("\nClassification Report:\n", classification_report(y_test, y_pred_test))
