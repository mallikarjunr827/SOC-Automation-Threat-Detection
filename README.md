-SOC Automation & Threat Detection-

A mini SOC prototype designed for **real-time SSH and honeypot log analysis**, automated threat detection, visualization, and interactive dashboards. This system demonstrates core **SOC operations**, including monitoring, alerting, reporting, and basic threat intelligence integration.

=> Features

->Real-time SSH login monitoring using honeypots** (e.g., Cowrie) to capture attacker IPs, usernames, and passwords.
->Automated threat detection rules**:
  - Failed login attempts exceeding threshold.
  - Multiple usernames per IP indicating reconnaissance or brute-force attempts.
  - Logins during unusual hours (midnight–6 AM) for anomaly detection.
  - Detection of brute-force patterns and repeated failed attempts before success.
->Interactive dashboards** built with Streamlit:
  - Visualize threat statistics with bar charts, line graphs, and IP-based threat summaries.
  - Filter alerts by IP, username, time, or type of attack.
->Automated reporting**:
  - Generates structured CSVs for detected alerts.
  - Produces PDF reports summarizing suspicious activity.
  - Optional email notifications for high-priority alerts.
->Extensible and modular code** for adding new detection rules or integrating with SIEM platforms.

=> Project Structure

SOC-Automation-Threat-Detection/
│
├── src/ # Python scripts
│ ├── log_ingest.py # Parse and normalize raw log files
│ ├── detect.py # Rule-based threat detection engine
│ ├── detectemail.py # Optional email alerting module
│ ├── detect_bruteforce.py # Brute-force detection enhancement
│ ├── report.py # PDF report generation
│ └── dashboard.py # Interactive Streamlit dashboard
│
├── data/ # Sample logs, parsed CSVs, PDF reports
│ ├── sample_logs/
│ ├── parsed_logs.csv
│ ├── alerts.csv
│ └── Mini_SIEM_Report.pdf
│
├── docs/ # Optional screenshots, architecture diagrams
└── README.md # Project documentation

=> Technical Details

->Log Sources: Honeypot logs (Cowrie), SSH auth logs, and custom generated logs.
->Detection Rules:  
  1. Failed Login Attempts – Trigger alert if `failed_attempts >= 2`.  
  2. Multiple Usernames per IP – Detects reconnaissance behavior.  
  3. Unusual Hour Login – Flags logins outside business hours (12 AM – 6 AM).  
  4. Brute-force Detection – Counts repeated failed attempts before a successful login.  
->Data Handling:
  - Python `pandas` for log parsing, aggregation, and merging multiple detection rules.  
  - CSV and JSON export for structured alert storage.  
->Visualization: Streamlit dashboard with:
  - Bar graphs of failed attempts per IP.
  - Usernames per source IP.
  - Login activity over time (hourly).
  - Filters for threat type, IP, username, or time range.
->Reporting:
  - PDFs generated using `fpdf` summarizing all alerts.
  - Configurable report templates.
->Automation & Extensibility:
  - Modular scripts allow easy addition of new detection rules.
  - Real-time monitoring through continuous log ingestion.
  - Optional email/SMS integration for high-severity alerts.
    
=>Future Enhancements

-Integration with Splunk, ELK Stack, or other SIEM platforms for full-scale monitoring.

-Real-time email/SMS alerting using APIs like Twilio, SendGrid, or SES.

-Cloud-based monitoring for AWS/Azure environments including CloudTrail and GuardDuty logs.

-Advanced threat intelligence feeds for automated IP and domain enrichment.

-Machine Learning-based anomaly detection for unusual login patterns.
