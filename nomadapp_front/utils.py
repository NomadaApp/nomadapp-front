import streamlit as st
import pandas as pd
import json
import numpy as np
import pandas_gbq
import logging

# Logging
logging.basicConfig(
    filename='nomadapp.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def on_click_info_button(api_data: dict, location: str, radius: int):
    """
    Receives a dictionary of the selected parameters by the user.
    This information will be used to make the request to Google API.

    Params:
        - api_data: dict expected, data from the Google Maps API
        - location, str expected, selected location by the user
    Return:
        - None if the address field is empty (no address to make the request)
    Raises:
        - TypeError if 'api_data' type is not dict
        - TypeError if 'location' type is not string
    """
    if isinstance(api_data, st.delta_generator.DeltaGenerator):
        logging.warning(f'Wrong api data type; expected dict, received {type(api_data)}')
        return None
    elif isinstance(api_data, dict):
        if api_data.get('Error'):
            logging.error('No results or incomplete information received from the API ')
            st.markdown(f'No results received from API. {api_data["Error"]}')
        if isinstance(location, str):
            # Building DataFrame from Dictionary
            # The received object is dict-type; converting to JSON
            json_object = json.dumps(api_data)
            df = pd.read_json(json_object)
            df = df[df["distance_from_location"] <= radius].reset_index(drop=True)
            # Showing selections
            location_list = location.split(" ")
            location = " ".join([location.capitalize() for location in location_list])
            st.markdown(f" ## *{location}*")
            for location_type in list(df.Type.value_counts().index):
                with st.expander(f"{location_type}"):
                    st.write(
                        f"There are {len(df[df.Type == location_type])} {location_type} places around your position"
                    )
            # Showing the map - Default zoom: 11
            st.map(df)
            df = df.drop(["lat", "lon", "coord"], axis=1)
            df.columns = ["Name", "Distance", "Rating", "Type"]
            # DataFrame visualization improving
            df['Rating'] = df['Rating'].astype(str).str[:3]
            st.write(df)
            df['Rating'] = pd.to_numeric(df['Rating'])
            try:
                df.to_gbq(
                    "nomadapp.user-queries",
                    project_id="cocktail-bootcamp",
                    if_exists="append",
                )
                logging.info('Data successfully ingested on BigQuery table')
            except:
                logging.warning("The data wasn't ingested on BigQuery table. The program continues.")
                pass
        else:
            st.markdown(f" ")
    else:
        st.markdown(f" ")
