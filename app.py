# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pickle
import pandas as pd


# Load trained model



model = pickle.load(
    open('MultipleLinearRegression.pkl', 'rb')
)
# Streamlit App


st.title("Toyota Corolla Price Prediction")
st.write("Multiple Linear Regression Model")

st.header("Enter Car Details")

# User Inputs
Age_08_04 = st.number_input(
    "Age of Car (months)",
    min_value=1,
    max_value=100,
    value=30
)

KM = st.number_input(
    "Kilometers",
    min_value=0,
    value=50000
)

HP = st.number_input(
    "Horse Power",
    min_value=50,
    max_value=300,
    value=110
)

cc = st.number_input(
    "Engine Capacity (cc)",
    min_value=500,
    max_value=5000,
    value=1600
)

Doors = st.number_input(
    "Number of Doors",
    min_value=2,
    max_value=5,
    value=4
)

Cylinders = st.number_input(
    "Number of Cylinders",
    min_value=2,
    max_value=12,
    value=4
)

Gears = st.number_input(
    "Number of Gears",
    min_value=3,
    max_value=8,
    value=5
)

Weight = st.number_input(
    "Weight (kg)",
    min_value=500,
    max_value=3000,
    value=1100
)

Automatic = st.selectbox(
    "Automatic",
    [0, 1]
)

Fuel_Type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

# Prediction


if st.button("Predict Price"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "Age_08_04": [Age_08_04],
        "KM": [KM],
        "HP": [HP],
        "Automatic": [Automatic],
        "cc": [cc],
        "Doors": [Doors],
        "Cylinders": [Cylinders],
        "Gears": [Gears],
        "Weight": [Weight],

        # One-hot encoded Fuel_Type
        "Fuel_Type_Diesel": [1 if Fuel_Type == "Diesel" else 0],
        "Fuel_Type_Petrol": [1 if Fuel_Type == "Petrol" else 0]
    })

    # IMPORTANT:
    # Arrange columns exactly as training data
    input_data = input_data[model.feature_names_in_]

    # Prediction
    prediction = model.predict(input_data)

    st.success(
        f"Predicted Toyota Corolla Price: € {prediction[0]:,.2f}"
    )
