import streamlit as st
import logging
from utils import on_click_info_button
from get_data_from_api import gcp_request_get


# 1. LOGGER .................................................................
logging.basicConfig(
    filename="nomadapp.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True,
)

# 2. STREAMLIT SETTINGS .....................................................
def config_page():
    """Streamlit main settings"""
    st.set_page_config(page_title="NomadApp", layout="wide")


# Cache
st.cache(suppress_st_warning=True)

# 3. FRONT-END FUNCTIONALITY .................................................


# Home
def home():
    """Home page of Streamlit Front-End"""
    st.markdown("# NomadApp")
    st.markdown("Welcome to NomadApp!")
    im = "https://aviationvoice.com/wp-content/uploads/2017/03/US-Electronics-Ban-To-Affect-18000-Daily-Passengers.jpg"
    st.image(im, caption="Working at the airport. Source: aviationvoice.com")


# Travel
def travel():
    """
    Widgets, SideBar Menu, buttons and settings of the 'Travel' page of
    Streamlit Front-End.

    The page has a left-side menu with 'Filters' -check-buttons- and a slider,
    to define the user's radio around his geo-position.
    The button 'Get Info' makes the call to the back-end API with the
    collected info via check-buttons and the 'Address' field, implemented on
    the main side of the page.

    All the data will be stored in a parameter dictionary, used as argument to
    make the request.

    When the user press the 'Get Info' button, this function makes a call to
    get_data_from_api/gcp_request_get function with the mentioned dictionary,
    and receives a json object.

    The last part of this function makes the call to utils/on_click_info_button,
    and plots the map and the information required by the user in Streamlit.
    """
    text_input = st.text_input("Search your address here")
    st.sidebar.markdown("### Filters:")

    leisure = st.sidebar.checkbox("Leisure")
    restaurants = st.sidebar.checkbox("Restaurants")
    education = st.sidebar.checkbox("Education")
    co_working = st.sidebar.checkbox("CoWorking")
    st.sidebar.markdown("\n")
    radius = st.sidebar.slider("Choose the radius (in km)", 1, 10)
    st.sidebar.markdown("\n\n\n\n")

    # Filters Dict - Default
    filters_dict = {
        "location": text_input,
        "leisure": False,
        "restaurants": False,
        "education": False,
        "coworking": False,
        "radius": None,
    }

    # Building the dictionary
    if leisure:
        filters_dict["leisure"] = True
    if restaurants:
        filters_dict["restaurants"] = True
    if education:
        filters_dict["education"] = True
    if co_working:
        filters_dict["coworking"] = True

    filters_dict["radius"] = radius * 1000

    # Info Button - Physical button
    info_button = st.sidebar.button(
        label="Get Info", help="Press to get your selected info"
    )
    # Click on info_button - Requesting data to Google API and showing the map
    if info_button:
        # requesting data
        logging.info("User requested information. Calling api_data function.")
        api_data = gcp_request_get(query=filters_dict)
        # showing the map with the received data
        logging.info("Calling on_click_info_button function.")
        on_click_info_button(api_data=api_data, location=text_input, radius=radius)
