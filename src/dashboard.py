import os
import pandas as pd

INPUT_FILE = os.path.join("data", "parsed_logs.csv")
OUTPUT_FILE = os.path.join("data", "alerts.csv")

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Parsed logs not found: {INPUT_FILE}")
        return

    df = pd.read_csv(INPUT_FILE)

    # Filter only "Failed password" events from SSH logs
    failed = df[df["message"].str.contains("Failed password", na=False)]

    if failed.empty:
        print("✅ No failed login attempts found.")
        return

    # Count failed attempts per IP
    alerts = (
        failed.groupby("source_ip")
        .agg(
            failed_attempts=("message", "count"),
            first_seen=("timestamp", "min"),
            last_seen=("timestamp", "max")
        )
        .reset_index()
    )

    # Flag only suspicious IPs with >1 failed attempt
    alerts = alerts[alerts["failed_attempts"] > 1]

    if alerts.empty:
        print("✅ No suspicious activity detected.")
    else:
        alerts.to_csv(OUTPUT_FILE, index=False)
        print(f"🚨 Detected {len(alerts)} suspicious IP(s) -> {OUTPUT_FILE}")
        print(alerts)

if __name__ == "__main__":
    main()
