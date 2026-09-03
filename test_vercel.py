import requests

vercel_url = "https://floodsense-mumbai-ok7l.vercel.app"

endpoints = ["/api/health", "/api/wards", "/api/news", "/api/historical"]

for ep in endpoints:
    url = vercel_url + ep
    try:
        res = requests.get(url, timeout=10)
        print(f"GET {ep} -> Status: {res.status_code}")
        print("Response (first 100 chars):", res.text[:100])
        print("-" * 40)
    except Exception as e:
        print(f"GET {ep} failed: {e}")
