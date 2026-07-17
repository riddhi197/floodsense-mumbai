import pandas as pd
import numpy as np
import openmeteo_requests
import requests_cache
from retry_requests import retry
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier
import pickle
import os

print("Starting training process for FloodSense ML Model...")

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# 1. Fetch historical weather data for Mumbai
print("Fetching historical weather data (2018-2024)...")
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 19.0760,
	"longitude": 72.8777,
	"start_date": "2018-01-01",
	"end_date": "2024-12-31",
	"daily": ["precipitation_sum", "rain_sum", "precipitation_hours"],
	"timezone": "Asia/Kolkata"
}

responses = openmeteo.weather_api(url, params=params)
response = responses[0]

daily = response.Daily()
daily_precipitation_sum = daily.Variables(0).ValuesAsNumpy()
daily_rain_sum = daily.Variables(1).ValuesAsNumpy()
daily_precipitation_hours = daily.Variables(2).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["precipitation_sum"] = daily_precipitation_sum
daily_data["rain_sum"] = daily_rain_sum
daily_data["precipitation_hours"] = daily_precipitation_hours

df = pd.DataFrame(data = daily_data)
df['date'] = df['date'].dt.tz_convert('Asia/Kolkata').dt.date

# 2. Add rolling features (soil saturation / antecedent moisture)
print("Engineering features...")
df['precip_3d_sum'] = df['precipitation_sum'].rolling(window=3, min_periods=1).sum().shift(1)
df['precip_7d_sum'] = df['precipitation_sum'].rolling(window=7, min_periods=1).sum().shift(1)
df.fillna(0, inplace=True)

# 3. Inject verified flood labels (Target variable)
flood_dates = [
    "2018-06-08", "2018-06-25", "2018-07-10",
    "2019-07-02", "2019-07-26", "2019-09-04",
    "2020-08-04", "2020-08-05", "2020-08-06", "2020-09-22", "2020-09-24",
    "2021-05-17", "2021-06-09", "2021-06-13", "2021-07-16", "2021-07-18", "2021-07-22",
    "2022-07-05", "2022-08-16", "2022-10-07",
    "2023-06-24", "2023-07-20", "2023-07-26", "2023-07-27",
    "2024-07-08", "2024-07-26"
]
flood_dates_parsed = [pd.to_datetime(d).date() for d in flood_dates]

df['is_flood'] = df['date'].apply(lambda x: 1 if x in flood_dates_parsed else 0)

# 4. Train the Model
print("Training XGBoost Classifier...")
features = ['precipitation_sum', 'precipitation_hours', 'precip_3d_sum', 'precip_7d_sum']
X = df[features]
y = df['is_flood']

# Correct Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Handle class imbalance on training set only
num_neg = len(y_train[y_train == 0])
num_pos = len(y_train[y_train == 1])
scale_weight = num_neg / max(num_pos, 1)

model = XGBClassifier(
    n_estimators=100, 
    max_depth=4, 
    learning_rate=0.1, 
    scale_pos_weight=scale_weight,
    random_state=42
)

model.fit(X_train, y_train)

# 5. Save the model
model_path = os.path.join(os.path.dirname(__file__), 'flood_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"Model successfully trained and saved to: {model_path}")

# 6. Evaluate Model on unseen test data
y_pred = model.predict(X_test)

print("\n--- Model Evaluation (Test Set) ---")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
print(f"F1-Score:  {f1_score(y_test, y_pred):.4f}")

correct_positives_train = sum((y_train == 1) & (model.predict(X_train) == 1))
print(f"\nCaptured {correct_positives_train}/{num_pos} known flood events in training data.")
correct_positives_test = sum((y_test == 1) & (y_pred == 1))
print(f"Captured {correct_positives_test}/{len(y_test[y_test == 1])} known flood events in testing data.")
