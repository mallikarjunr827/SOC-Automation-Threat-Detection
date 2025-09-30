# src/dashboard2.py
import streamlit as st
import pandas as pd
import os
import plotly.express as px

ALERTS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "alerts_bruteforce.csv")

alerts = pd.read_csv(ALERTS_FILE)

st.set_page_config(page_title="Mini-SIEM Dashboard", layout="wide")
st.title("Mini-SIEM Interactive Dashboard")

# Download button
st.download_button(
    label="Download Brute-Force Alerts CSV",
    data=alerts.to_csv(index=False).encode('utf-8'),
    file_name='alerts_bruteforce.csv',
    mime='text/csv'
)

st.subheader("Brute-Force Alerts")
st.dataframe(alerts)
