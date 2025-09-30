# src/geoip.py
import requests

def get_ip_location(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        data = response.json()
        if data["status"] == "success":
            return {
                "ip": ip,
                "country": data.get("country", "Unknown"),
                "city": data.get("city", "Unknown"),
                "lat": data.get("lat", 0),
                "lon": data.get("lon", 0),
            }
    except Exception as e:
        return {"ip": ip, "country": "Unknown", "city": "Unknown", "lat": 0, "lon": 0}
