

import requests

# DATA FROM GOOGLE API
def gcp_request_get():
    url = "https://nomadapp-back-akukb5qdcq-ew.a.run.app/json-request"
    response = requests.get(url, json=None)
    return response.json()


req_json = gcp_request_get()