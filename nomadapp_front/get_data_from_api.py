

import requests
import streamlit as st


# DATA FROM GOOGLE API
def gcp_request_get(query: dict):
    """
    Makes a request to the back-end API with a list of parameters,
    passed as dictionary.

    The request returns the required information by the user, based on
    the selected address.

    This functions returns a dictionary with the requested data from
    Google API.

    Params:
        - query: dict expected, dictionary with the request parameters.

    Returns:
        - st.delta_generator.DeltaGenerator object: if bad request
        - Dictionary with the received data from the API: if the request
        was successfully made
    """
    # Back-End API URL
    url = "https://nomadapp-back-akukb5qdcq-ew.a.run.app/json-request"
    # Making the request with the collected parameters
    response = requests.get(url, params=query)
    # Exceptions - Bad Requests
    if str(response) == '<Response [500]>':
        return st.markdown(f"### The address seems to be wrong or incomplete.")
    elif str(response).startswith('<Response [4'):
        return st.markdown(f"### The address seems to be wrong or incomplete.")
    # Returns a dictionary with the collected data, if the request was successfully
    try:
        return eval(response.json())
    except TypeError:
        st.markdown("### The address seems to be wrong or incomplete.")
