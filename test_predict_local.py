from fastapi.testclient import TestClient
from api.index import app

client = TestClient(app)

# Test Mumbai Prediction
mumbai_payload = {
    "scope": "mumbai",
    "rain_today": 120.5,
    "rain_3d": 250.0,
    "rain_7d": 400.0,
    "rain_hours": 12.0,
    "month_val": 7
}
response = client.post("/api/predict", json=mumbai_payload)
print("Mumbai Test Response status:", response.status_code)
print("Mumbai Test Response JSON:", response.json())
print("-" * 50)

# Test Konkan Prediction
konkan_payload = {
    "scope": "konkan",
    "rain_today": 200.0,
    "rain_3d": 450.0,
    "rain_7d": 700.0,
    "rain_hours": 0.0,
    "month_val": 8
}
response = client.post("/api/predict", json=konkan_payload)
print("Konkan Test Response status:", response.status_code)
print("Konkan Test Response JSON:", response.json())
