import pandas as pd
import numpy as np
import pickle
import os
import sqlite3
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

# Path setup
db_path = 'floodsense.db'
model_path = 'floodsense_final_model.pkl'

print("--- Step 1: Loading Rainfall Data ---")
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
cursor.execute("UPDATE rainfall_daily SET Confirmed_Event = 0;")
for d in flood_dates:
    cursor.execute("UPDATE rainfall_daily SET Confirmed_Event = 1 WHERE Date = ?;", (d,))
conn.commit()

df = pd.read_sql('SELECT * FROM rainfall_daily', conn)

features = ['Rainfall_mm', 'Rainfall_3day', 'Rainfall_7day', 'Month']
X = df[features]
y = df['Confirmed_Event'] # Predict actual verified events

# Perform 80/20 Train-Test Split (stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("--- Step 2: Training Advanced Stacking Ensemble ---")
# Set scale_pos_weight for XGBoost to balance classes
num_neg = sum(y_train == 0)
num_pos = sum(y_train == 1)
scale_weight = num_neg / max(num_pos, 1)

# Base estimators
base_estimators = [
    ('rf', RandomForestClassifier(n_estimators=100, max_depth=3, class_weight='balanced', random_state=42)),
    ('xgb', XGBClassifier(n_estimators=100, max_depth=3, scale_pos_weight=scale_weight, random_state=42, eval_metric='logloss'))
]

# Meta-learner (Balanced Logistic Regression)
meta_learner = LogisticRegression(class_weight='balanced', random_state=42)

# Stacking Classifier
stack_model = StackingClassifier(
    estimators=base_estimators,
    final_estimator=meta_learner,
    cv=5,
    n_jobs=-1
)

# Fit on training data only
stack_model.fit(X_train, y_train)

# Evaluate
y_pred_train = stack_model.predict(X_train)
y_pred_test = stack_model.predict(X_test)
acc_train = accuracy_score(y_train, y_pred_train)
acc_test = accuracy_score(y_test, y_pred_test)

print(f"Stacking Ensemble Training Accuracy: {acc_train:.4f}")
print(f"Stacking Ensemble Testing Accuracy (Unseen Data): {acc_test:.4f}")

# Save Model Bundle
bundle = {
    "model": stack_model,
    "label_encoder": None,
    "features": features
}
with open(model_path, 'wb') as f:
    pickle.dump(bundle, f)
print(f"Saved advanced ensemble model to: {model_path}")

print("--- Step 3: Probabilistic Clustering using Gaussian Mixture Models (GMM) ---")
df_wards = pd.read_sql('SELECT * FROM ward_risk', conn)

# Features for GMM clustering
X_wards = df_wards[['Known_Flood_Spots_Count', 'Population_At_Risk_Pct']].copy()
scaler = StandardScaler()
X_wards_scaled = scaler.fit_transform(X_wards)

# GMM with 3 components (Low, Medium, High risk)
gmm = GaussianMixture(n_components=3, covariance_type='full', random_state=42)
gmm.fit(X_wards_scaled)

# Predict hard clusters and soft probabilities
clusters = gmm.predict(X_wards_scaled)
probs = gmm.predict_proba(X_wards_scaled)

# Map clusters to risk categories based on actual spots count
# We want the cluster with highest average flood spots to be 'High', lowest to be 'Low'
cluster_means = [X_wards.iloc[clusters == i]['Known_Flood_Spots_Count'].mean() for i in range(3)]
sorted_indices = np.argsort(cluster_means)
cluster_map = {sorted_indices[0]: 0, sorted_indices[1]: 1, sorted_indices[2]: 2} # 0=Low, 1=Medium, 2=High
mapped_clusters = [cluster_map[c] for c in clusters]
labels_map = {0: 'Low', 1: 'Medium', 2: 'High'}
mapped_labels = [labels_map[c] for c in mapped_clusters]

# Re-order probabilities accordingly
gmm_probs_low = probs[:, sorted_indices[0]]
gmm_probs_med = probs[:, sorted_indices[1]]
gmm_probs_high = probs[:, sorted_indices[2]]

# Write GMM results to database
df_wards['Cluster'] = mapped_clusters
df_wards['Cluster_Label'] = mapped_labels
df_wards['GMM_Prob_Low'] = gmm_probs_low
df_wards['GMM_Prob_Med'] = gmm_probs_med
df_wards['GMM_Prob_High'] = gmm_probs_high

# Update ward_risk table in database
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS ward_risk;")
df_wards.to_sql('ward_risk', conn, index=False)
conn.commit()
conn.close()

print("Database successfully updated with GMM probabilistic profiles!")
