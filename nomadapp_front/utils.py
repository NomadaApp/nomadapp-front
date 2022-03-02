

import streamlit as st
import pandas as pd
import json


# TODO: el argumento son los datos recibidos de la API de Rubén
# BUILDING NEW FUNCTION ON-CLICK ####################################

def on_click_info_button(api_data: dict, location: str):
    """
    Receives a dictionary of the selected parameters by the user.
    This information will be used to make the request to Google API.

    Params:
        - filters: dict expected,
    Return:
        - filters: dict, parameters to make the request
    Raises:
        - TypeError if 'filters' type is not dict
    """
    if isinstance(api_data, dict):
        if isinstance(location, str):
            # Building DataFrame from Dictionary
            # The received object is dict-type; converting to JSON
            json_object = json.dumps(api_data)
            df = pd.read_json(json_object)

            # Showing selections
            st.markdown(f' ## *{location}*')
            st.markdown('### SELECTED FILTERS:')
            for location_type in list(df.Type.value_counts().index):
                st.markdown(f'#### - {location_type}')
            # Showing the map - Default zoom: 11
            st.map(df, zoom=11)
        else:
            raise TypeError(f'Str expected, received {type(location)}.')
    else:
        raise TypeError(f'Dict expected, received {type(api_data)}.')





