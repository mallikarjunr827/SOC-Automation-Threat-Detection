import streamlit as st
import pandas as pd
import os
import plotly.express as px
from geoip import get_ip_location   # our helper

# File path
ALERTS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "alerts_bruteforce.csv")

# Load alerts
alerts = pd.read_csv(ALERTS_FILE)

st.set_page_config(page_title="Mini-SIEM Dashboard", layout="wide")
st.title("Mini-SIEM Interactive Dashboard")

# GeoIP lookup
geo_data = []
for ip in alerts['source_ip'].unique():
    geo_data.append(get_ip_location(ip))

geo_df = pd.DataFrame(geo_data)

st.subheader("🌍 Attacker IPs on World Map")
st.map(geo_df[['lat', 'lon']])

# Show alerts table
st.subheader("Brute-Force Alerts")
st.dataframe(alerts)
# Group attacks by country
country_counts = geo_df['country'].value_counts().reset_index()
country_counts.columns = ['country', 'attack_count']

st.subheader("📊 Top Attacker Countries")
fig_country = px.bar(
    country_counts.head(5),
    x='country',
    y='attack_count',
    title="Top 5 Attacker Countries",
    color='attack_count'
)
st.plotly_chart(fig_country, use_container_width=True)
# Dropdown filter for country
selected_country = st.selectbox("Filter by Country", options=["All"] + list(geo_df['country'].unique()))

if selected_country != "All":
    filtered_alerts = alerts[alerts['source_ip'].isin(
        geo_df[geo_df['country'] == selected_country]['ip']
    )]
else:
    filtered_alerts = alerts
# --- FILTERS SECTION ---
st.subheader("🔎 Filter Alerts")

# Country filter
countries = ["All"] + list(geo_df['country'].unique())
selected_country = st.selectbox("Filter by Country", options=countries, key="country_filter")

# IP filter (only IPs from selected country, or all if 'All')
if selected_country == "All":
    ips = ["All"] + list(alerts['source_ip'].unique())
else:
    ips = ["All"] + list(geo_df[geo_df['country'] == selected_country]['ip'])

selected_ip = st.selectbox("Filter by IP", options=ips, key="ip_filter")

# Apply filters
filtered_alerts = alerts.copy()
if selected_country != "All":
    filtered_alerts = filtered_alerts[filtered_alerts['source_ip'].isin(
        geo_df[geo_df['country'] == selected_country]['ip']
    )]

if selected_ip != "All":
    filtered_alerts = filtered_alerts[filtered_alerts['source_ip'] == selected_ip]

# Show filtered results
st.subheader(f"Filtered Alerts ({selected_country}, {selected_ip})")
st.dataframe(filtered_alerts)
# --- DATE FILTER ---
st.subheader("📅 Filter by Date Range")

# Make sure timestamp is in datetime format
alerts['timestamp'] = pd.to_datetime(alerts['timestamp'], errors='coerce')

# Get min and max dates
min_date = alerts['timestamp'].min().date()
max_date = alerts['timestamp'].max().date()

# Let user pick a date range
date_range = st.date_input(
    "Select Date Range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date,
    key="date_filter"
)

# Apply filter
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered_alerts = filtered_alerts[
        (filtered_alerts['timestamp'].dt.date >= start_date) &
        (filtered_alerts['timestamp'].dt.date <= end_date)
    ]
