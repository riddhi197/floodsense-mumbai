import pickle
import os
import sqlite3
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve

base_dir = "."
db_path = 'floodsense.db'
model_path = 'floodsense_final_model.pkl'

# 1. Load data
conn = sqlite3.connect(db_path)
df = pd.read_sql('SELECT * FROM rainfall_daily', conn)
conn.close()

features = ['Rainfall_mm', 'Rainfall_3day', 'Rainfall_7day', 'Month']
X = df[features]
y = df['Confirmed_Event']

# Split identical to train_advanced.py
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 2. Load model
with open(model_path, 'rb') as f:
    bundle = pickle.load(f)
model = bundle['model']

# 3. Predict probabilities on test set
probs = model.predict_proba(X_test)[:, 1]

# 4. Compute Precision-Recall Curve
precisions, recalls, thresholds = precision_recall_curve(y_test, probs)

# Calculate F1-score for each threshold
f1_scores = 2 * (precisions * recalls) / (precisions + recalls + 1e-8)
best_idx = np.argmax(f1_scores)
best_threshold = thresholds[best_idx]
best_f1 = f1_scores[best_idx]
best_precision = precisions[best_idx]
best_recall = recalls[best_idx]

print(f"Optimal Threshold (Max F1-Score): {best_threshold:.4f}")
print(f"Precision at this threshold: {best_precision:.4f}")
print(f"Recall at this threshold: {best_recall:.4f}")
print(f"F1-Score at this threshold: {best_f1:.4f}")
