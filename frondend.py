import streamlit as st
import requests
from main import available_locations

API_URL="http://127.0.0.1:8000/predict"

st.title("Housing Price Prediction")

st.markdown("Enter the details")
location=sorted(available_locations)

selected_location = st.selectbox(
    "Select Location",
    location,
    index=None,
    placeholder="Location of house "
)
BHK= st.number_input("BHK of the House")
bath= st.number_input("No of BathRooms")
total_sqft= st.number_input(" Total Squrefeet of the House ")

if st.button("Predict Price"):
    if selected_location is None:
        st.error("Please select a location")
    else:
        payload = {
            "location": selected_location,
            "BHK": int(BHK),
            "bath": int(bath),
            "total_sqft": float(total_sqft)
        }
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Predicted Price: {result['predicted_price']}")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Connection error: {str(e)}")



