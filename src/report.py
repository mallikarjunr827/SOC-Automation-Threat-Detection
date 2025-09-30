# src/report.py
import pandas as pd
from fpdf import FPDF
import os

# Paths
ALERTS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "alerts.csv")
CHART_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "alerts_chart.png")
PDF_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "Mini_SIEM_Report.pdf")

# Read alerts
alerts = pd.read_csv(ALERTS_FILE)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Mini-SIEM Threat Detection Report", ln=True, align="C")

pdf.ln(10)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, "Suspicious IPs and Failed Login Attempts:", ln=True)

# Add table
pdf.set_font("Arial", '', 12)
pdf.ln(5)
for i, row in alerts.iterrows():
    pdf.cell(0, 8, f"{i+1}. {row['source_ip']} - {row['failed_attempts']} failed attempts", ln=True)

# Add chart image
pdf.ln(10)
pdf.cell(0, 10, "Bar Chart of Failed Attempts:", ln=True)
pdf.image(CHART_FILE, w=160)

# Save PDF
pdf.output(PDF_FILE)
print(f"PDF report saved as {PDF_FILE}")
