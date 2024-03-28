import pandas as pd
import requests
from streamlit_folium import folium_static
import streamlit as st

# Secret key for API adress
url = st.secrets["http://127.0.0.1:8000/docs"]

# Streamlit app title

st.markdown(
    "<h1 style='text-align: center;'>Real Estate Price Prediction</h1><br>",
    unsafe_allow_html=True,
)


dataLocality = pd.read_csv("data/locality_zip_codes.csv")


# sylvan Order:

col1, spacer, col2 = st.columns([1, 0.25, 1])

with col1:
    subproperty_type_dict = {
        "APARTMENT": "Apartment",
        "HOUSE": "House",
        "APARTMENT_BLOCK": "Apartment Block",
        "BUNGALOW": "Bungalow",
        "CASTLE": "Castle",
        "CHALET": "Chalet",
        "COUNTRY_COTTAGE": "Country Cottage",
        "EXEPTIONAL_PROPERTY": "Exceptional Property",
        "DUPLEX": "Duplex",
        "FARMHOUSE": "Farmhouse",
        "FLAT_STUDIO": "Flat Studio",
        "GROUND_FLOOR": "Ground Floor",
        "LOFT": "Loft",
        "KOT": "Kot",
        "MANOR_HOUSE": "Manor House",
        "MANSION": "Mansion",
        "MIXED_USE_BUILDING": "Mixed Use Building",
        "PENTHOUSE": "Penthouse",
        "SERVICE_FLAT": "Service Flat",
        "TOWN_HOUSE": "Town House",
        "TRIPLEX": "Triplex",
        "VILLA": "Villa",
        "OTHER_PROPERTY": "Other Property",
    }

    switched_dict = {value: key for key, value in subproperty_type_dict.items()}

    subproperty_type_key = st.selectbox("Property Type", list(switched_dict.keys()))
    subproperty_type_value = switched_dict[subproperty_type_key]

    if subproperty_type_value in (
        "APARTMENT",
        "DUPLEX",
        "FLAT_STUDIO",
        "GROUND_FLOOR",
        "KOT",
        "LOFT",
        "PENTHOUSE",
        "SERVICE_FLAT",
        "TRIPLEX",
    ):
        property_type = "APARTMENT"
    else:
        property_type = "HOUSE"

    locality = st.selectbox(
        "Locality",
        (
            "Aalst",
            "Antwerp",
            "Arlon",
            "Ath",
            "Bastogne",
            "Brugge",
            "Brussels",
            "Charleroi",
            "Dendermonde",
            "Diksmuide",
            "Dinant",
            "Eeklo",
            "Gent",
            "Halle-Vilvoorde",
            "Hasselt",
            "Huy",
            "Ieper",
            "Kortrijk",
            "Leuven",
            "Liège",
            "Maaseik",
            "Marche-en-Famenne",
            "Mechelen",
            "Mons",
            "Mouscron",
            "Namur",
            "Neufchâteau",
            "Nivelles",
            "Oostend",
            "Oudenaarde",
            "Philippeville",
            "Roeselare",
            "Sint-Niklaas",
            "Soignies",
            "Thuin",
            "Tielt",
            "Tongeren",
            "Tournai",
            "Turnhout",
            "Verviers",
            "Veurne",
            "Virton",
            "Waremme",
        ),
    )
    if locality:
        data = dataLocality[dataLocality["locality"] == f"{locality}"]
        zip_code = st.selectbox("ZIP Code", data["zip_code"].to_list())
    construction_year = st.number_input(
        "Construction Year", value=2000, min_value=1800, max_value=2024
    )
    total_area_sqm = st.number_input(
        "Total Living Area in m²", value=150, min_value=10, max_value=1000
    )
    epc = st.selectbox(
        "Energy Performance Certificate",
        ("A++", "A+", "A", "B", "C", "D", "E", "F", "G", "Unknown"),
    )
    if epc == "Unknown":
        epc = "MISSING"

    equipped_kitchen = st.checkbox(
        "Is your kitchen equipped?",
    )
    state_building = st.checkbox(
        "Property renovated in the last 2 years?",
    )

with col2:
    nbr_bedrooms = st.slider("Number of Bedrooms", value=3, min_value=1, max_value=10)
    surface_land_sqm = st.slider(
        "Total land area in m²", value=150, min_value=10, max_value=1000
    )
    nbr_frontages = st.slider("Number of Frontages", value=1, min_value=0, max_value=5)

    fl_terrace = st.checkbox("Terrace", value=True)
    if fl_terrace:
        terrace_sqm = st.slider(
            "Terrace Area in m²", value=20, min_value=10, max_value=100
        )
    else:
        terrace_sqm = 0
    fl_garden = st.checkbox("Garden", value=True)
    if fl_garden:
        garden_sqm = st.slider(
            "Garden Area in m²", value=80, min_value=10, max_value=1000
        )
    else:
        garden_sqm = 0
    fl_swimming_pool = st.checkbox("Swimming Pool")
    fl_double_glazing = st.checkbox("Double Glazing")
    fl_open_fire = st.checkbox("Open Fire")


# Input manualy this
# latitude = 0
# longitude = 0
# primary_energy_consumption_sqm = 0
# cadastral_income = 0
payload = {
    "num_features": {
        "construction_year": construction_year,
        "total_area_sqm": total_area_sqm,
        "surface_land_sqm": surface_land_sqm,
        "nbr_frontages": nbr_frontages,
        "nbr_bedrooms": nbr_bedrooms,
        "terrace_sqm": terrace_sqm,
        "garden_sqm": garden_sqm,
        "zip_code": zip_code,
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
        "kitchen_clusterized": "Yes" if equipped_kitchen else "No",
        "state_building_clusterized": "Yes" if state_building else "No",
        "epc": epc,
    },
}

print(payload)
prediction = 0

col1, col2, col3, col4 = st.columns([0.5, 2, 2, 2])
with col2:

    # Button to send the request
    if st.button("Predict Price"):
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                # Display the prediction result
                prediction = response.json()
                print(prediction["Prediction of price"])

            else:
                # Handle errors
                st.error(f"Failed to get response: {response.status_code}")
                print(response.text)
        except Exception as e:

            st.error(f"An error occurred: {str(e)}")

with col3:
    see_map = st.button("Discover Matching Homes")
with col4:
    see_map_neighboorhood = st.button("View Neighborhood Map")

col1, col2, col3 = st.columns([1, 2, 1])

if prediction:
    st.markdown(
        f'<div style="text-align:center; font-size:24px; background-color:darkgreen; color:white; padding:10px; border-radius:10px;">Your property price : {prediction["Prediction of price"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown("")
    st.markdown(
        f'<div style="text-align:center; font-size:24px; background-color:darkorange; color:white; padding:10px; border-radius:10px;">Confidence Interval : {prediction["Price range based on model accuracy"]}</div>',
        unsafe_allow_html=True,
    )

error = False

   
            

            