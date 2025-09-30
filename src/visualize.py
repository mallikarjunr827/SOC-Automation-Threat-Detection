# src/visualize.py
import pandas as pd
import matplotlib.pyplot as plt
import folium
import os

# Paths
ALERTS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "alerts.csv")
MAP_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "alerts_map.html")

# Read alerts
alerts = pd.read_csv(ALERTS_FILE)

# --- Bar chart of failed attempts per IP ---
plt.figure(figsize=(8,5))
plt.bar(alerts['source_ip'], alerts['failed_attempts'], color='red')
plt.title('Suspicious IPs - Failed Login Attempts')
plt.xlabel('Source IP')
plt.ylabel('Failed Attempts')
plt.savefig(os.path.join(os.path.dirname(__file__), "..", "data", "alerts_chart.png"))
plt.show()

# --- Map of suspicious IPs ---
# Simple geolocation (for demo, use dummy coordinates)
# In real project, use GeoIP database or API
ip_coords = {
    '203.0.113.10': [37.7749, -122.4194],  # Example coordinates (San Francisco)
    '198.51.100.5': [40.7128, -74.0060]    # Example coordinates (New York)
}

m = folium.Map(location=[39.5, -98.35], zoom_start=4)  # Center of USA
for ip in alerts['source_ip']:
    coords = ip_coords.get(ip, [0,0])
    folium.Marker(location=coords, popup=f"{ip}: {alerts.loc[alerts['source_ip']==ip, 'failed_attempts'].values[0]} attempts").add_to(m)

# Save map
m.save(MAP_FILE)
print(f"Bar chart saved as alerts_chart.png")
print(f"Map saved as alerts_map.html")
