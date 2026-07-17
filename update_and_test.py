import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, recall_score

db_path = 'C:/Users/User/Downloads/FloodSense_Mumbai/FloodSense_Mumbai/floodsense.db'
conn = sqlite3.connect(db_path)

# Update database to set Confirmed_Event = 1 for the 24 monsoon flood dates
flood_dates = [
    "2018-06-08", "2018-06-25", "2018-07-10",
    "2019-07-02", "2019-07-26", "2019-09-04",
    "2020-08-04", "2020-08-05", "2020-08-06", "2020-09-22", "2020-09-24",
    "2021-06-09", "2021-06-13", "2021-07-16", "2021-07-18", "2021-07-22",
    "2022-07-05", "2022-08-16",
    "2023-06-24", "2023-07-20", "2023-07-26", "2023-07-27",
    "2024-07-08", "2024-07-26"
]

cursor = conn.cursor()
# Reset all first
cursor.execute("UPDATE rainfall_daily SET Confirmed_Event = 0;")
# Set the 24 dates
for d in flood_dates:
    cursor.execute("UPDATE rainfall_daily SET Confirmed_Event = 1 WHERE Date = ?;", (d,))
conn.commit()

# Reload data
df = pd.read_sql('SELECT * FROM rainfall_daily', conn)
conn.close()

features = ['Rainfall_mm', 'Rainfall_3day', 'Rainfall_7day', 'Month']
X = df[features]
y = df['Confirmed_Event']

print("Total days in dataset:", len(y))
print("Updated Confirmed flood days in dataset:", sum(y))

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Set scale_pos_weight
num_neg = sum(y_train == 0)
num_pos = sum(y_train == 1)
scale_weight = num_neg / max(num_pos, 1)

base_estimators = [
    ('rf', RandomForestClassifier(n_estimators=100, max_depth=3, class_weight='balanced', random_state=42)),
    ('xgb', XGBClassifier(n_estimators=100, max_depth=3, scale_pos_weight=scale_weight, random_state=42, eval_metric='logloss'))
]

meta_learner = LogisticRegression(class_weight='balanced', random_state=42)

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
