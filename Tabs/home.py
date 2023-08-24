"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Air Quality Detector")

    # Add image to the home page
    st.image('images/home.png')

    st.subheader("What is AQI?")

    st.write("An air quality index or AQI is used by government agencies to communicate to the public how polluted the air currently is or how polluted it is forecast to become. Public health risks increase as the AQI rises. Different countries have their own air quality indices, corresponding to different national air quality standards")
    
    
    st.write('The purpose of the AQI is to help people know how the local air quality impacts their health.')
    

    st.markdown("""
    * **Pollutants(Features) that we are going to analyze and use for prediction:** 
        * **so2:** The amount of Sulphur Dioxide measured.
        * **no2:** The amount of Nitrogen Dioxide measured
        * **rspm:** Respirable Suspended Particulate Matter measured.
        * **spm:** Suspended Particulate Matter measured.
        * **pm2_5:** It represents the value of particulate matter measured.
    """)
    st.subheader("AQI Category")
    st.write('AQI can be divided into few category based on their AQI values. Each category has its own related to its impact on the envionment.')
    
    st.image("aqirange.jpg")
  
