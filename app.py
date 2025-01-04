import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

# Set the app title
st.title("Real-Time Air Quality Index (AQI) Visualization")

# App description
st.write("""
This app visualizes the Air Quality Index (AQI) for various cities in India.
It highlights:
- **Green Zones:** Areas with low AQI (good air quality).
- **Red Zones:** Areas with high AQI (poor air quality).
""")

# Load AQI data (CSV file from Colab)
st.header("AQI Data Overview")
try:
    aqi_data = pd.read_csv("india_aqi_data_all_states.csv")
    st.dataframe(aqi_data)
except FileNotFoundError:
    st.error("The AQI data file ('india_aqi_data_all_states.csv') is missing. Please upload it to your repository.")

# Display the interactive map (HTML file from Colab)
st.header("Interactive AQI Map")
try:
    map_file = "red_green_zone_map.html"
    st_folium(map_file, width=800, height=600)
except FileNotFoundError:
    st.error("The map file ('red_green_zone_map.html') is missing. Please upload it to your repository.")

# Optionally, display additional features like predictions
st.header("LSTM Predictions (Optional)")
try:
    predictions = pd.read_csv("lstm_aqi_predictions.csv")
    st.dataframe(predictions)
except FileNotFoundError:
    st.info("LSTM predictions file ('lstm_aqi_predictions.csv') not found. Add it for more insights.")
