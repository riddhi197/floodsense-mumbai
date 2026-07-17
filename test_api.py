import requests
import json

base_url = "http://127.0.0.1:8000"

try:
    # Test Health
    res_health = requests.get(f"{base_url}/api/health")
    print("Health API status:", res_health.json())
    
    # Test Prediction (Mumbai Model)
    payload_mumbai = {
        "scope": "mumbai",
        "rain_today": 120.0,
        "rain_3d": 150.0,
        "rain_7d": 300.0,
        "rain_hours": 14.5,
        "month_val": 7
    }
    res_predict = requests.post(f"{base_url}/api/predict", json=payload_mumbai)
    print("\nMumbai Prediction Output:", json.dumps(res_predict.json(), indent=2))
    
    # Test Wards Fetch
    res_wards = requests.get(f"{base_url}/api/wards")
    print(f"\nWards Loaded: {len(res_wards.json())} entries.")
    
except Exception as e:
    print("API connection test failed:", e)
