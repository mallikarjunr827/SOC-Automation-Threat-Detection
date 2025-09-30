import pandas as pd
import os

# Paths
INPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "parsed_logs.csv")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "alerts_bruteforce.csv")

# Read parsed logs
df = pd.read_csv(INPUT_FILE)

# --- Identify brute-force attempts ---
# Failed logins grouped by IP
failed_counts = df[df['event'] == 'cowrie.login.failed'].groupby('source_ip').size().reset_index(name='failed_attempts')

# Multiple usernames per IP
multi_user = df.groupby('source_ip')['username'].nunique().reset_index(name='username_count')

# Failed then success sequences
df['failed'] = df['event'].apply(lambda x: 1 if 'failed' in x else 0)
success_seq = df[df['event'] == 'cowrie.login.success'].groupby('source_ip')['failed'].sum().reset_index(name='failed_before_success')

# Combine all
alerts = pd.merge(failed_counts, multi_user, on='source_ip', how='outer')
alerts = pd.merge(alerts, success_seq, on='source_ip', how='outer')
alerts = alerts.fillna(0)

# Save enhanced brute-force alerts
alerts.to_csv(OUTPUT_FILE, index=False)
print(f"Brute-force alerts saved -> {OUTPUT_FILE}")
print(alerts)
