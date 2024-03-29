import pandas as pd
import requests
import time
import streamlit as st

# Display the logo and app title
with st.sidebar:
    st.image("streamlit/images/logo.webp", width=100)

st.image("streamlit/images/header.webp", width=100)
st.title("Price Prediction API")

# Thin horizontal divider line
horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"
st.markdown(horizontal_bar, True)
st.subheader("How much is your home worth?")
st.markdown("Price prediction is based on a Machine Learning Model generated from collecting +75,000 listings in Belgium.")

# Load data
dataLocality = pd.read_csv("data/locality_zip_codes.csv")

# API address 
url = "https://immo-eliza-deployment-xzpq.onrender.com/docs"

# User input layout
col1, spacer, col2 = st.columns([1, 0.25, 1])

with col1:
    # Define property type selections
    subproperty_type_dict = {
        "APARTMENT": "Apartment",
        "HOUSE": "House",
        # Add other types...
    }

    # Reverse dictionary for display purposes
    switched_dict = {value: key for key, value in subproperty_type_dict.items()}
    subproperty_type_key = st.selectbox("Property Type", list(switched_dict.keys()))
    subproperty_type_value = switched_dict[subproperty_type_key]

    # Determine main property type
    if subproperty_type_value in ("APARTMENT", "DUPLEX", "FLAT_STUDIO", "GROUND_FLOOR", "LOFT", "PENTHOUSE", "SERVICE_FLAT"):
        property_type = "APARTMENT"
    else:
        property_type = "HOUSE"

    # Locality selection
    locality = st.selectbox("Locality", sorted(dataLocality["locality"].unique()))
    zip_code = st.selectbox("ZIP Code", dataLocality[dataLocality["locality"] == locality]["zip_code"].unique())

    # Other property attributes
    construction_year = st.number_input("Construction Year", value=2000, min_value=1800, max_value=2024)
    total_area_sqm = st.number_input("Total Living Area in m²", value=150, min_value=10, max_value=1000)
    epc = st.selectbox("Energy Performance Certificate", ("A++", "A+", "A", "B", "C", "D", "E", "F", "G", "Unknown"))

with col2:
    # Additional property attributes
    nbr_bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
    surface_land_sqm = st.slider("Total land area in m²", 10, 1000, 150)
    nbr_frontages = st.slider("Number of Frontages", 0, 5, 2)
    fl_terrace = st.checkbox("Terrace", value=True)
    fl_garden = st.checkbox("Garden", value=True)
    fl_swimming_pool = st.checkbox("Swimming Pool")
    fl_double_glazing = st.checkbox("Double Glazing")
    fl_open_fire = st.checkbox("Open Fire")

# Construct payload for the API request
payload = {
    "num_features": {
        "construction_year": construction_year,
        "total_area_sqm": total_area_sqm,
        "surface_land_sqm": surface_land_sqm,
        "nbr_frontages": nbr_frontages,
        "nbr_bedrooms": nbr_bedrooms,
        "zip_code": int(zip_code),
    },
    "fl_features": {
        "fl_terrace": int(fl_terrace),
        "fl_open_fire": int(fl_open_fire),
        "fl_swimming_pool": int(fl_swimming_pool),
        "fl_garden": int(fl_garden),
        "fl_double_glazing": int(fl_double_glazing),
    },
    "cat_features": {
        "property_type": property_type,
        "subproperty_type": subproperty_type_value,
        "locality": locality,
        "epc": "MISSING" if epc == "Unknown" else epc,
    },
}

# Button to send the request and display the prediction
if st.button("Predict Price"):
    with st.spinner("Getting predictions..."):
        time.sleep(1)  # Simulate a delay for user feedback
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Predicted Price: {prediction['predicted_price']} €")
        else:
            st.error("Failed to get prediction from the API. Please try again later.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")