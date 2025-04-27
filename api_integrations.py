#--------------------------
# API Integration Functions
#--------------------------

import requests # To handle HTTPS requests for utilizing APIs.
from config import MAPBOX_TOKEN, CLIMATIQ_API_KEY, ZYLA_API_KEY

def geocode_location(place_name, mapbox_token):
    """
    Get the longitude and latitude for a place name using the Mapbox Geocoding API. 
    Returning the latitude and longitude as a dictionary, or None if no coordinates were found. 
    """
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"
    # Construct the URL for the Mapbox Geocoding API. 

    parameters = {
        "access_token": mapbox_token, # Add the access token for authentication in the query parameters.
        "limit": 1 # Limiting the results to only the one, top match.
    }
    
    response = requests.get(url, parameters=parameters)
    # Make the GET request to the Mapbox API.

    if response.status_code == 200:
        data = response.json()
        features = data.get("features")
        if features:
            coordinates = features[0]["geometry"]["coordinates"]
            return {"longitude": coordinates[0], 
                    "latitude": coordinates[1]
            }
        else:
            print(f"No results found for:{place_name}")
    
    else:
        print(f"Error:", response.status_code, response.text)
        return None 

def get_travel_emissions(distance_km, mode, climatiq_api_key):
    """
    Estimate CO2 emissions for each user's individual trips using the 
    Climatiq API. 
    Returning the calculate Kilograms of CO2 emitted, or None if failed. 
    """
    url = "https://beta3.api.climatiq.io/travel"
    headers = {
        "Authorization": f"Bearer {climatiq_api_key}",
        "Content-Type":"application/json"
    }
    payload = {
        "distance": {"value": distance_km, "unit": "km"}, "transport_mode": mode
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        emissions_kg = data.get("co2e", None) # Extract emissions in KG CO2e.
        return {"emissions_kg": emissions_kg, "source": "climatiq"}
    else:
        print(f"Error {response.status_code}:{response.text}")

    return None

def get_zyla_carbon_footprint(distance_km, mode, zyla_api_key):
    """
    Calculate user's carbon footprint using the Zyla API.
    Returning the calculate Kilograms of CO2 emitted, or None if failed. 
    """ 
    url = "https://zylalabs.com/api/824/tracker+for+carbon+footprint+api/583/calculate+carbon+footprint"
    headers = {
        "Authorization": f"Bearer {zyla_api_key}",
        "Content-Type":"application/json"
    }
    payload = {
        "distance": distance_km,
        "unit": "km",
        "transport_mode": mode
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        emissions_kg = data.get("emissions", None)

        return {"emissions_kg":emissions_kg, "source": "zyla"}
    else:
        print(f"Error {response.status_code}:{response.text}")

        return None