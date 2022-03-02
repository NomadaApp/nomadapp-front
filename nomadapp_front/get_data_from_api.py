

import requests


# DATA FROM GOOGLE API
def gcp_request_get(filters_dict):
    url = "https://nomadapp-back-akukb5qdcq-ew.a.run.app/json-request"
    response = requests.get(url, params=filters_dict)
    return response.json()

