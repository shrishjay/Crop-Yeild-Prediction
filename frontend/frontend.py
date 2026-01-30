import streamlit as st
import requests

with st.container():
    st.subheader("Welcome to the AI Crop Yeild Prediction software")
    st.write("Just provide the neccessary details about the crop and the weather")
with st.container():
    st.write("---")
    State_Name = st.selectbox(
        "State Name",
        [
            "andhra pradesh",
            "arunachal pradesh",
            "assam",
            "bihar",
            "goa",
            "gujarat",
            "haryana",
            "jammu and kashmir",
            "karnataka",
            "kerala",
            "madhya pradesh",
            "maharashtra",
            "manipur",
            "meghalaya",
            "mizoram",
            "nagaland",
            "odisha",
            "punjab",
            "rajasthan",
            "tamil nadu",
            "telangana",
            "uttar pradesh",
            "west bengal",
            "chandigarh",
            "dadra and nagar haveli",
            "himachal pradesh",
            "puducherry",
            "sikkim",
            "tripura",
            "andaman and nicobar islands",
            "chhattisgarh",
            "uttarakhand",
            "jharkhand",
        ],
    )
    Crop_Type = st.selectbox("Crop Type", ["kharif", "rabi", "summer", "whole year"])
    Crop = st.selectbox(
        "Crop",
        [
            "cotton",
            "horsegram",
            "jowar",
            "maize",
            "moong",
            "ragi",
            "rice",
            "sunflower",
            "wheat",
            "sesamum",
            "soyabean",
            "rapeseed",
            "jute",
            "arecanut",
            "onion",
            "potato",
            "sweetpotato",
            "tapioca",
            "turmeric",
            "barley",
            "banana",
            "coriander",
            "garlic",
            "blackpepper",
            "cardamom",
            "cashewnuts",
            "ladyfinger",
            "brinjal",
            "grapes",
            "mango",
            "orange",
            "tomato",
            "papaya",
            "pineapple",
            "cabbage",
        ],
    )
    N = st.number_input("Nitrogen Amount in Soil", 0, 100)
    P = st.number_input("Phosphorus Amount in Soil", 0, 100)
    K = st.number_input("Potassium Amount in Soil", 0, 100)
    pH = st.number_input("pH of the soil", 0, 14)
    rainfall = st.number_input("rainfall in mm", 0, 500)
    temperature = st.number_input("temperature of the region in Centigrades", 0, 60)
    if st.button(
        "Predict yeild per hectare",
    ):
        input_data = {
            "State_Name": State_Name,
            "Crop_Type": Crop_Type,
            "Crop": Crop,
            "N": N,
            "P": P,
            "K": K,
            "pH": pH,
            "rainfall": rainfall,
            "temperature": temperature,
        }
        # After input_data = {...}

        # Show loading state
        with st.spinner("Predicting yield..."):
            try:
                # Make POST request to FastAPI
                response = requests.post(
                    "http://backend:8000/predict",  # Your FastAPI URL
                    json=input_data,  # Send the data
                    headers={"Content-Type": "application/json"},
                )

                # Check if request was successful
                if response.status_code == 200:
                    # Get the prediction from response
                    result = response.json()
                    prediction = result["predicted yeild per hectare"]

                    # Display result
                    st.success(f"Predicted Yield: {prediction} per hectare")
                else:
                    # Show error if request failed
                    st.error(f"Error: {response.status_code} - {response.text}")

            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to FastAPI server. Make sure it's running on localhost:8000"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
