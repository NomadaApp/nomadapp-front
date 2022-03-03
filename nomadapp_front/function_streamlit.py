import requests
import streamlit as st
from utils import on_click_info_button
from get_data_from_api import gcp_request_get


# 1. STREAMLIT SETTINGS ...............................................
def config_page():
    st.set_page_config(page_title="NomadApp", layout="wide")


# Cache
st.cache(suppress_st_warning=True)


# 2. SAMPLE DATA ......................................................

# Output Data - Sample
output_data = {
    "Name": {
        "0": "IES Eijo and Garay",
        "1": "IES Ortega y Gassett",
        "2": "IES El Lago",
        "3": "IES Gran Capit\u00e1n",
        "4": "IES Emilio Castelar",
        "5": "I.E.S. SAN ISIDRO",
        "6": "IES Blas de Otero",
        "7": "IES Gerardo Diego",
        "8": "IES Iturralde",
        "9": "I.E.S. Renacimiento",
        "10": "Ies Santa Teresa De Jes\u00fas",
        "11": "I.E.S. Mariano Jos\u00e9 de Larra (High-school)",
        "12": "Secondary Bilingual Cervantes Institute",
        "13": "IES Cardenal Cisneros",
        "14": "I.E.S. PARK ALUCHE",
        "15": "IES Santa Teresa de Jesus",
        "16": "IES Isaac Newton",
        "17": "Instituto San Isidoro de Sevillla",
        "18": "IES Empress Maria of Austria",
        "19": "I.E.S. Juan de La Cierva"},
    "lat": {
        "0": 40.4080381,
        "1": 40.4316436,
        "2": 40.4156612,
        "3": 40.4036056,
        "4": 40.3883572,
        "5": 40.4126691,
        "6": 40.3890626,
        "7": 40.443267,
        "8": 40.3861044,
        "9": 40.3936682,
        "10": 40.4206152,
        "11": 40.3878669,
        "12": 40.4059367,
        "13": 40.424465,
        "14": 40.3904061,
        "15": 40.4204545,
        "16": 40.4730134,
        "17": 40.4455389,
        "18": 40.3875901,
        "19": 40.4023011},
    "lon": {
        "0": -3.7385759,
        "1": -3.7357291,
        "2": -3.7328165,
        "3": -3.7199915,
        "4": -3.7302832,
        "5": -3.7073444,
        "6": -3.7621458,
        "7": -3.787076,
        "8": -3.751705,
        "9": -3.7384516,
        "10": -3.7107258,
        "11": -3.7538598,
        "12": -3.7031812,
        "13": -3.7085845,
        "14": -3.76395,
        "15": -3.7103158,
        "16": -3.7214324,
        "17": -3.7187209,
        "18": -3.7168563,
        "19": -3.7063803},
    "Type": {
        "0": "Education",
        "1": "Education",
        "2": "Education",
        "3": "Education",
        "4": "Education",
        "5": "Education",
        "6": "Education",
        "7": "Education",
        "8": "Education",
        "9": "Education",
        "10": "Education",
        "11": "Education",
        "12": "Education",
        "13": "Education",
        "14": "Education",
        "15": "Education",
        "16": "Education",
        "17": "Education",
        "18": "Education",
        "19": "Education"}}


# 3. FRONT-END FUNCTIONALITY ..........................................


# Home
def home():
    st.markdown("# NomadApp")
    st.markdown("Welcome to NomadApp!")


# Travel
def travel():
    text_input = st.text_input("Search your address here")
    st.sidebar.markdown("### Filters:")

    leisure = st.sidebar.checkbox("Leisure")
    restaurants = st.sidebar.checkbox("Restaurants")
    education = st.sidebar.checkbox("Education")
    co_working = st.sidebar.checkbox("CoWorking")
    st.sidebar.markdown("\n")
    radius = st.sidebar.slider("Choose the radius (in km)", 1, 10)
    st.sidebar.markdown("\n\n\n\n")


    # TODO: Building filters_dict

    # Filters Dict - Default
    filters_dict = {
        'location': text_input,
        'leisure': False,
        'restaurants': False,
        'education': False,
        'coworking': False,
        'radius': None}

    if leisure:
        filters_dict['leisure'] = True
    if restaurants:
        filters_dict['restaurants'] = True
    if education:
        filters_dict['education'] = True
    if co_working:
        filters_dict['coworking'] = True

    filters_dict['radius'] = radius

    # Info Button - Physical button
    info_button = st.sidebar.button(label='Get Info',
                                    help='Press to get your selected info')
    # Click on info_button - Requesting data to Google API and showing the map
    if info_button:
        # requesting data
        # TODO: implementar cuando exista comunicación efectiva
        api_data = gcp_request_get(filters_dict)
        # showing the map with the received data
        # TODO: implementar cuando exista comunicación efectiva
        on_click_info_button(api_data=api_data, location=text_input)
        # on_click_info_button(api_data=output_data,
        #                      location=text_input)


