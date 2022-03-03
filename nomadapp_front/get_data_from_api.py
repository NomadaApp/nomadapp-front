

import requests
import json
import streamlit as st

filters_dict = {
        'location': 'Puerta del Sol, 1 Madrid',
        'leisure': True,
        'restaurants': True,
        'education': True,
        'coworking': True,
        'radius': 5}


# DATA FROM GOOGLE API
def gcp_request_get(query):
    url = "https://nomadapp-back-akukb5qdcq-ew.a.run.app/json-request"
    response = requests.get(url, params=query)
    if str(response) == '<Response [500]>':
        return st.markdown("## Error. Internal Server Error. Can't get required information")
    return eval(response.json())



