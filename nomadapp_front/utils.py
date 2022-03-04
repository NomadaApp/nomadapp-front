import streamlit as st
import pandas as pd
import json
import pandas_gbq


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
        return None
    elif isinstance(api_data, dict):
        if isinstance(location, str):
            # Building DataFrame from Dictionary
            # The received object is dict-type; converting to JSON
            json_object = json.dumps(api_data)
            df = pd.read_json(json_object)
            df = df[df["distance_from_location"] <= radius].reset_index(drop=True)
            # Showing selections
            st.markdown(f" ## *{location}*")
            for location_type in list(df.Type.value_counts().index):
                with st.expander(f"{location_type}"):
                    st.write(
                        f"There are {len(df[df.Type == location_type])} {location_type} places around your position"
                    )
            # Showing the map - Default zoom: 11
            st.map(df)
            df = df.drop(["lat", "lon"], axis=1)
            df.columns = ["Name", "Position", "Distance", "Type"]
            st.write(df)
            df["Position"] = ", ".join(df["Position"])[1:-1]
            df.to_gbq(
                "nomadapp.user-queries",
                project_id="cocktail-bootcamp",
                if_exists="append",
            )
        else:
            raise TypeError(f"Str expected, received {type(location)}.")
    else:
        raise TypeError(f"Dict expected, received {type(api_data)}.")
