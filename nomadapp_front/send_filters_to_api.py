

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

root_path = "http://127.0.0.1:5000"

filters_dict = {
    'leisures': False,
    'activities': False,
    'schools': False,
    'beach_mountain': False,
    'coworking': False,
    'radio': 5}


@app.route("/filters_request", methods=['GET'])
def get_filters(data=filters_dict):
    response = request.get_json()
    return jsonify(data)


app.run(host="0.0.0.0")








