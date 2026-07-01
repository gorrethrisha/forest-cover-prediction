import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("forest_cover_model.pkl")

# Title
st.title(" Forest Cover Type Prediction")
st.write("Enter important geographical and environmental information to predict forest cover type.")

# User Inputs
elevation = st.number_input("Elevation", min_value=0, value=3000)
roadways = st.number_input("Horizontal Distance To Roadways", min_value=0, value=1000)
fire_points = st.number_input("Horizontal Distance To Fire Points", min_value=0, value=1000)
hydrology_horizontal = st.number_input("Horizontal Distance To Hydrology", min_value=0, value=100)
hydrology_vertical = st.number_input("Vertical Distance To Hydrology", value=0)

hillshade_9am = st.number_input("Hillshade 9am", min_value=0, max_value=255, value=220)
aspect = st.number_input("Aspect", min_value=0, max_value=360, value=180)
hillshade_3pm = st.number_input("Hillshade 3pm", min_value=0, max_value=255, value=150)
hillshade_noon = st.number_input("Hillshade Noon", min_value=0, max_value=255, value=230)

slope = st.number_input("Slope", min_value=0, max_value=90, value=10)

wilderness_area4 = st.selectbox("Wilderness Area 4", [0, 1])
wilderness_area1 = st.selectbox("Wilderness Area 1", [0, 1])

soil_type10 = st.selectbox("Soil Type 10", [0, 1])
soil_type3 = st.selectbox("Soil Type 3", [0, 1])
soil_type38 = st.selectbox("Soil Type 38", [0, 1])

# Prediction
if st.button("Predict Forest Cover Type"):

    # Create all model features with default value 0
    input_dict = {
        'Elevation': 0,
        'Aspect': 0,
        'Slope': 0,
        'Horizontal_Distance_To_Hydrology': 0,
        'Vertical_Distance_To_Hydrology': 0,
        'Horizontal_Distance_To_Roadways': 0,
        'Hillshade_9am': 0,
        'Hillshade_Noon': 0,
        'Hillshade_3pm': 0,
        'Horizontal_Distance_To_Fire_Points': 0,
        'Wilderness_Area1': 0,
        'Wilderness_Area2': 0,
        'Wilderness_Area3': 0,
        'Wilderness_Area4': 0
    }

    # Add Soil Types
    for i in range(1, 41):
        input_dict[f'Soil_Type{i}'] = 0

    # Update important features
    input_dict['Elevation'] = elevation
    input_dict['Aspect'] = aspect
    input_dict['Slope'] = slope
    input_dict['Horizontal_Distance_To_Hydrology'] = hydrology_horizontal
    input_dict['Vertical_Distance_To_Hydrology'] = hydrology_vertical
    input_dict['Horizontal_Distance_To_Roadways'] = roadways
    input_dict['Hillshade_9am'] = hillshade_9am
    input_dict['Hillshade_Noon'] = hillshade_noon
    input_dict['Hillshade_3pm'] = hillshade_3pm
    input_dict['Horizontal_Distance_To_Fire_Points'] = fire_points
    input_dict['Wilderness_Area1'] = wilderness_area1
    input_dict['Wilderness_Area4'] = wilderness_area4
    input_dict['Soil_Type3'] = soil_type3
    input_dict['Soil_Type10'] = soil_type10
    input_dict['Soil_Type38'] = soil_type38

    input_df = pd.DataFrame([input_dict])

    prediction = model.predict(input_df)

    cover_labels = {
        1: "Spruce/Fir",
        2: "Lodgepole Pine",
        3: "Ponderosa Pine",
        4: "Cottonwood/Willow",
        5: "Aspen",
        6: "Douglas-fir",
        7: "Krummholz"
    }

    result = cover_labels[prediction[0]]

    st.success(f"Predicted Forest Cover Type: {result}")