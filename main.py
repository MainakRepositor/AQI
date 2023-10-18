"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, predict
# Configure the app
st.set_page_config(
    page_title = 'Air Quality Detector',
    page_icon = ':wind:',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "Prediction": predict  
}
# Real time AQI measure
st.sidebar.markdown(
    f'<a href="https://aqi-tsa.streamlit.app/" target="_blank" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">TIme Series AQI Measure</a>',
    unsafe_allow_html=True
)

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))


# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Prediction"]:
    Tabs[page].app(df, X, y)

else:
    Tabs[page].app()
