import streamlit as st
import requests

def main():
    st.title('Immoliza: Property Price Predictor!')
    st.write("This calculator helps you estimate the price of a property based on various factors. "
             "Please select the type of property and its amenities to get started.")
    st.markdown('##### Choose some features to start the price prediction')

    # Property type selection 
    property_type_options = ['', 'House', 'Apartment']
    property_type = st.selectbox(
        "Property Type:",
        property_type_options,
        index=0,
        format_func=lambda x: "Select Property Type" if x == '' else x + " 🏠" if x == "House" else x + " 🏢" if x == "Apartment" else x)

    # Latitude and Longitude (To Replace with a map)
    col1, col2 = st.columns(2)
    with col1:
        latitude = st.number_input('Latitude', value=0.0, format="%.5f")
    with col2:
        longitude = st.number_input('Longitude', value=0.0, format="%.5f")

    # Region and Zip Code
    col1, col2 = st.columns(2)
    with col1:
        region_options = ['', 'Brussels', 'Flanders', 'Wallonia']
        region = st.selectbox('Region', region_options, index=0, format_func=lambda x: "Select Region" if x == '' else x)
    with col2:
        zip_code = st.text_input('ZIP Code', '')

    # Locality and Subproperty Type
    col1, col2 = st.columns(2)
    locality_options = ['', 'Aalst', 'Antwerp', 'Arlon', 'Ath', 'Bastogne', 'Brugge', 'Brussels', 
                        'Charleroi', 'Dendermonde', 'Diksmuide', 'Dinant', 'Eeklo', 'Gent', 
                        'Halle-Vilvoorde', 'Hasselt', 'Huy', 'Ieper', 'Kortrijk', 'Leuven', 
                        'Liege', 'Maaseik', 'Marche-en-Famenne', 'Mechelen', 'Mons', 'Mouscron', 
                        'Namur', 'Neufchateau', 'Nivelles', 'Oostend', 'Oudenaarde', 'Philippeville', 
                        'Roeselare', 'Sint-Niklaas', 'Soignies', 'Thuin', 'Tielt', 'Tongeren', 'Tournai', 
                        'Turnhout', 'Verviers', 'Veurne', 'Virton', 'Waremme']
    with col1:
        locality = st.selectbox('Locality', locality_options, index=0, format_func=lambda x: "Select Locality" if x == '' else x)
    subproperty_type_options = ['', 'APARTMENT', 'APARTMENT_BLOCK', 'BUNGALOW', 'CHALET', 'COUNTRY_COTTAGE', 
                                'DUPLEX-TRIPLEX', 'EXCEPTIONAL_PROPERTY_MANOR_HOUSE_CASTEL', 'FARMHOUSE', 
                                'FLAT_STUDIO_KOT', 'GROUND_FLOOR', 'HOUSE', 'LOFT_PENTHOUSE', 'MANSION', 
                                'MIXED_USE_BUILDING', 'OTHER_PROPERTY', 'SERVICE_FLAT', 'TOWN_HOUSE', 'VILLA']
    with col2:
        subproperty_type = st.selectbox('Subproperty Type', subproperty_type_options, index=0, format_func=lambda x: "Select Subproperty Type" if x == '' else x)
    # Total Area and Bedrooms
    total_area_sqm = st.slider('Total Area (sqm)', min_value=0, max_value=1000, value=120)
    nbr_bedrooms = st.slider('Number of Bedrooms', min_value=0, max_value=10, value=2)

    # Advanced options expander
    with st.expander("Select more features to improve the prediction accuracy."):
        st.markdown("##### Energy and Construction Details")
        col1, col2 = st.columns(2)
        with col1:
            primary_energy_consumption_sqm = st.number_input('Primary Energy Consumption (kWh/m² year)', min_value=0, max_value=10000, step=10)
        with col2:
            all_years = list(range(1900, 2101))
            construction_year = st.selectbox('Choose a year', all_years)

        # Boolean features
        st.markdown("##### Amenities")
        col1, col2 = st.columns(2)
        with col1:
            fl_garden = st.checkbox('Garden')
            fl_terrace = st.checkbox('Terrace')
        with col2:
            fl_swimming_pool = st.checkbox('Swimming Pool')
            fl_floodzone = st.checkbox('Flood Zone')

    input_data = {
                'property_type': property_type if property_type != '' else None,
                'latitude': latitude if latitude != 0.0 else None,
                'longitude': longitude if longitude != 0.0 else None,
                'region': region if region != '' else None,
                'zip_code': zip_code if zip_code != '' else None,
                'locality': locality if locality != '' else None,
                'subproperty_type': subproperty_type if subproperty_type != '' else None,
                'total_area_sqm': total_area_sqm,
                'nbr_bedrooms': nbr_bedrooms,
                'primary_energy_consumption_sqm': primary_energy_consumption_sqm if primary_energy_consumption_sqm > 0 else None,
                'construction_year': construction_year if construction_year > 0 else None,
                'fl_garden': fl_garden,
                'fl_terrace': fl_terrace,
                'fl_swimming_pool': fl_swimming_pool,
                'fl_floodzone': fl_floodzone

            }
    # Predict button
    if st.button('Predict the property price'):        
        url = "https://immo-eliza-deployment-xzpq.onrender.com/predict"
        # Sending None for the fields that are not filled by the user
        for key in input_data.keys():
            if isinstance(input_data[key], str) and not input_data[key].strip():
                input_data[key] = None

        with st.spinner('Predicting...'):
             # POST request to the API
            response = requests.post(url, json=input_data)
            try:
                if response.status_code == 200:
                    prediction = response.json()['predicted_price']
                    st.success(f'Predicted Property Price: ${prediction:.2f}')
            except Exception as ex:
                print('error: ' + str(ex))
                st.error(ex)
          

if __name__ == '__main__':
    main()