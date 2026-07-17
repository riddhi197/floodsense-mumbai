import pandas as pd
import pickle
import os
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

db_path = os.path.join(os.path.dirname(__file__), 'floodsense.db')
model_path = os.path.join(os.path.dirname(__file__), 'floodsense_final_model.pkl')

with open(model_path, 'rb') as f:
    bundle = pickle.load(f)
    
model = bundle['model']
le = bundle['label_encoder']
features = bundle['features']

conn = sqlite3.connect(db_path)
df = pd.read_sql('SELECT * FROM rainfall_daily', conn)
conn.close()

X = df[features]
y = df['Flood_Severity']
y_encoded = le.transform(y)

# Perform the exact same split to isolate the true unseen test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

# Evaluate on Full Dataset
y_pred_all_num = model.predict(X)
y_pred_all = le.inverse_transform(y_pred_all_num)
print("=== OVERALL DATASET PERFORMANCE ===")
print(f"Accuracy: {accuracy_score(y, y_pred_all):.4f}")
print('\nClassification Report:\n', classification_report(y, y_pred_all))

# Evaluate on Test Split
y_pred_test_num = model.predict(X_test)
y_pred_test = le.inverse_transform(y_pred_test_num)
print("\n=== UNSEEN TEST SET PERFORMANCE (20% split) ===")
print(f"Accuracy: {accuracy_score(le.inverse_transform(y_test), y_pred_test):.4f}")
print('\nClassification Report:\n', classification_report(le.inverse_transform(y_test), y_pred_test))
