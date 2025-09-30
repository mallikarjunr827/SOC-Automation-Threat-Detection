# src/log_ingest.py
import os
import json
import pandas as pd

# Paths
INPUT_FOLDER = os.path.join(os.path.dirname(__file__), "..", "data", "sample_logs")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "parsed_logs.csv")

all_logs = []

# Read all JSON files in sample_logs
for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".json"):
        with open(os.path.join(INPUT_FOLDER, filename), "r", encoding="utf-8") as f:
            data = json.load(f)
            for entry in data:
                all_logs.append({
                    "timestamp": entry.get("timestamp"),
                    "source_ip": entry.get("src_ip"),
                    "username": entry.get("username"),
                    "password": entry.get("password"),
                    "event": entry.get("eventid")
                })

# Convert to DataFrame and save as CSV
df = pd.DataFrame(all_logs)
df.to_csv(OUTPUT_FILE, index=False)
print(f"Parsed {len(df)} rows -> {OUTPUT_FILE}")
