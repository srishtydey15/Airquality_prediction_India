import streamlit as st
import joblib
import numpy as np

model = joblib.load("aqi_model.pkl")

st.title("AQI Prediction")

SOi = st.number_input("SOi")
Noi = st.number_input("Noi")
Rpi = st.number_input("Rpi")
SPMi = st.number_input("SPMi")

if st.button("Predict AQI"):
    input_data = np.array([[SOi, Noi, Rpi, SPMi]])

    prediction = model.predict(input_data)

    st.success(f"Predicted AQI: {prediction[0]}")