"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of AQI Level. However, unlike normal prediction systems, the AQI Level parameter is alone sufficient to predict the remedy. But we still suggest to work with the other parameters as well, for a better relativity.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    so2 = st.slider("Sulphur Dioxide Level", int(df["so2"].min()), int(df["so2"].max()))
    no2 = st.slider("Nitrogen Dioxide Level", int(df["no2"].min()), int(df["no2"].max()))
    rspm = st.slider("Respirable Suspended Particulate Matter", int(df["rspm"].min()), int(df["rspm"].max()))
    spm = st.slider("Suspended Particulate Matter", float(df["spm"].min()), float(df["spm"].max()))
    pm2_5 = st.slider("Particulate Matter 2.5", float(df["pm2_5"].min()), float(df["pm2_5"].max()))
    nh3 = st.slider("Ammonia Level", float(df["nh3"].min()), float(df["nh3"].max()))
    o3 = st.slider("Ozone Level", float(df["o3"].min()), float(df["o3"].max()))
    co = st.slider("Carbon Monoxide Level", float(df["co"].min()), float(df["co"].max()))
    SPMi = st.slider("Suspended Particulate Matter Index", float(df["SPMi"].min()), float(df["SPMi"].max()))
    PMi = st.slider("Particulate Matter Index", float(df["PMi"].min()), float(df["PMi"].max()))
    aqi = st.slider("Air Quality Index", float(df["aqi"].min()), float(df["aqi"].max()))
 

    # Create a list to store all the features
    features = [so2,no2,rspm,spm,pm2_5,nh3,o3,co,SPMi,PMi,aqi]

    
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("AQI level detected...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The air quality is good. 😎")
        elif (prediction == 2):
            st.success("The air quality is medium. 😀")
            

        elif (prediction == 3):
            st.error("The air quality is poor and unhealthy. 😐🍃")
            

        elif (prediction == 4):
            st.error("The air quality is very unhealthy. 😫❗")
            

        else:
            st.error("The air quality is hazardous. 😵‍💫")
            
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by environmetal scientists and has an accuracy of ", (score*100),"%")


