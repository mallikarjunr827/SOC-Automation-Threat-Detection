-SOC Automation & Threat Detection-

A mini SOC prototype for real-time SSH and honeypot log analysis, automated threat detection, visualization, and interactive dashboards with real-time alerts and reports.

-> Features
- Real-time SSH login monitoring using honeypots.
- Automated detection of suspicious activity:
  - Failed login attempts
  - Multiple usernames per IP
  - Logins during unusual hours
- Interactive dashboards and bar graphs for threat visualization.
- Automated PDF reporting for alerts.
- Optional email notifications for detected threats.

-> Project Structure
SOC-Automation-Threat-Detection/
│
├── src/ # Python scripts for log ingestion, detection, dashboard, reporting
├── data/ # Sample logs, parsed CSVs, PDF reports
├── docs/ # Optional: screenshots, diagrams
└── README.md # This file

bash
Copy code
streamlit run src/dashboard.py
Future Enhancements
Integration with Splunk/ELK Stack for full SIEM simulation.

Real-time email/SMS alerting using external APIs.

Cloud-based monitoring using AWS/Azure.
