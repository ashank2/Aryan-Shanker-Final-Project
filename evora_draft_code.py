# This file was the initial start to my final project, 
# a rough draft to start my thinking process in regards to creating the MVP. 

# Afterwards, I accurately created seperate .py files - for greater organization
# and effectively altered and completed their functional codes.

# The API Integration Functions Part of this code script was altered completely. 
# Adjustments were made to the Importing APIs section of the code (config.py)
# as well as to the Adding The Machine Learning Library Stack section (ml_functions.py).

# I wanted to include this to show the first steps towards completing my final project.

#--------------------------------------
# Solidifying & Importing Relevant APIs
#--------------------------------------
import os
import requests # To handle HTTPS requests for utilizing APIs.
from dotenv import load_dotenv # Loading environmental variables from .env file.

# Load environment variables from .env file (contains the API Keys)
load_dotenv()

# Get API keys from environment variables:
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
CLIMATIQ_API_KEY = os.getenv("CLIMATIQ_API_KEY")

# For debugging purposes:
# print("MAPBOX_TOKEN", MAPBOX_TOKEN)
# print("CLIMATIQ_API_KEY", CLIMATIQ_API_KEY)

#------------------------------------------
# Adding The Machine Learning Library Stack
#------------------------------------------
# pandas: For data manipulation and analysis, especially for Tabular Data. 
import pandas as pd

# numpy: For efficient numerial computations.
import numpy as np

# scikit-learn: For classic machine learning algorithms, model selection, and pre-processing.
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score

# matplotlib: For visualizing data and results (ex: in chart & graphical forms).
import matplotlib.pyplot as plt

#--------------------------
# API Integration Functions
#--------------------------

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

#------------------
# Main Test & Usage
#------------------
if __name__ == "__main__":
    coordinates = geocode_location("Boston", MAPBOX_TOKEN)
    print("Coordinates of Boston:", coordinates)

    emissions_climatiq = get_travel_emissions(150, "car", CLIMATIQ_API_KEY)
    print("Climatiq emissions:", emissions_climatiq)

