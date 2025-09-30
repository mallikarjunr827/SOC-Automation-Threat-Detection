import os
import pandas as pd
import re

# Input log file (raw SSH logs)
INPUT_FILE = os.path.join("data", "sample_logs", "auth.log")
# Output parsed CSV
OUTPUT_FILE = os.path.join("data", "parsed_logs.csv")

# Regex pattern for SSH auth logs
LOG_PATTERN = re.compile(
    r'^(?P<timestamp>\w{3}\s+\d+\s[\d:]+).*sshd\[\d+\]:\s(?P<message>.*)$'
)

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        return {
            "timestamp": match.group("timestamp"),
            "message": match.group("message")
        }
    return None

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Log file not found: {INPUT_FILE}")
        return

    rows = []
    with open(INPUT_FILE, "r") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                # Extract IP if available
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', parsed["message"])
                parsed["source_ip"] = ip_match.group(1) if ip_match else None
                rows.append(parsed)

    if rows:
        df = pd.DataFrame(rows)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"✅ Parsed {len(df)} rows -> {OUTPUT_FILE}")
    else:
        print("⚠️ No log lines parsed.")

if __name__ == "__main__":
    main()
