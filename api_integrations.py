#--------------------------
# API Integration Functions
#--------------------------

import requests # Import requests library to handle HTTPS requests for utilizing APIs.
from config import MAPBOX_TOKEN, CLIMATIQ_API_KEY # From config.py import our APIs.  

def geocode_location(place_name, mapbox_token=MAPBOX_TOKEN):
    """
    Utilization of the Mapbox Geocoding API to get the coordinates (longitude, latitude) of 
    a place. 

    
    place_name (str): The name of the location to geocode.
    mapbox_token (str): Mapbox API 

    Returning the latitude and longitude as a dictionary, or None if no coordinates were found. 
    """
    # Build the endpoint URL for the Mapbox API to perform its function (Geocoding), 
    # using the place name provided by the user. 
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"

    #  Used AI for debugging in the below lines (line 26 - 29).
    #  Set up the parameters for the API Geocoding GET Request:
    # "access_token" is needed for authentication. "limit" restricts the results to the one, top match.
    params = {
        "access_token": mapbox_token, 
        "limit": 1 
    }
    
    # Error Handling:
    # Used AI for debugging in the below lines (line 34, line 38, line 52 - 54).
    try:
        response = requests.get(url, params=params, timeout=5)
        # Make the GET request to the Mapbox API, with specified parameters. 
        # Setting a waiting time of 5 seconds for the function to complete.

        response.raise_for_status()
        # If the function wasn't successful, raise an HTTP error.

        data = response.json()
        # Analyze the JSON response from the API.
        
        features = data.get("features")
        # Retrieve the geocoding results from the "features" list.

        if features:
            # If results are produced, extract coordinates from the first result:
            coordinates = features[0]["geometry"]["coordinates"]

            return {"longitude": coordinates[0], "latitude": coordinates[1]}
            # Return the coordinates of the place as a dictionary with longitude and latitude. 

        else:
            print(f"No results found for:{place_name}")
            # If no results are produced, print a "no results found" message. 
    
    except requests.RequestException as e:
        print(f"Mapbox API Error: {e}")
        # Print the error that occurs during the API request.

    return None
    # Return None if the API request does not work, or if no coordinates are found for the specific place. 

def get_travel_emissions(distance_km, mode, climatiq_api_key=CLIMATIQ_API_KEY):
    """
    Estimate CO2 emissions for each user's individual trips using the 
    Climatiq API. 
    
    distance_km (float): The distance travelled in kilometres.
    mode (str): Mode of transport (ex: 'car', 'train' etc.)
    climatiq_api_key (str): Climatiq API

    Returning the calculated Kilograms of CO2 emitted, or None if failed. 
    """
    
    # Build the endpoint URL for the Climatiq API to perform its function (emissions calculation).
    url = "https://beta3.api.climatiq.io/travel"
    
    #  Used AI for debugging in the below lines (line 83 - 89).
    #  Set up the HTTP headers, once again calling the API for authentication.
    headers = {
        "Authorization": f"Bearer {climatiq_api_key}",
        "Content-Type":"application/json"
    }
    # Create the payload (data to send) for the POST request. 
    # "distance" is a dictionary specifying the value and the unit. 
    # "transport_mode" is the type of transportation used by the user (ex: car, train). 
    payload = {
        "distance": {"value": distance_km, "unit": "km"}, "transport_mode": mode
    }
    
    # Error Handling: 
    # Similar to the code used above in the get_location function. 
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        # Make the POST request to the Climatiq API, with the headers and payload (data to send), 
        # setting a waiting time of 5 seconds for the function to complete.

        response.raise_for_status()
        # If the function wasn't successful, raise an HTTP error.

        data = response.json()
        # Analyze the JSON response from the API.

        emissions_kg = data.get("co2e", None) 
        # Extract the CO2e value, representing the kilograms of CO2 of emissions emitted.

        return {"emissions_kg": emissions_kg, "source": "climatiq"}
        # Return the emissions calculated as a dictionary, including the data source (in this case Climatiq). 

    except requests.RequestException as e:
        print(f"Climatiq API Error: {e}")
        # Print the error that occurs during the API request.

    return None
    # Return None if the API request does not work, or if emissions couldn't be calculated for the specified trip.

# Testing the functions above, for users: 
if __name__ == "__main__":

    # Ask the user to enter their starting location:
    place = input("Enter your starting location: ")
    coords = geocode_location(place) # Call the geocode_location function to get coordinates from user's input.
    print("Coordinates:", coords) # Print the coordinates (longitude, latitude) to the user. 

    # Ask the user to enter the distance they travelled in kilometres.
    distance = float(input("Enter distance travelled (km):"))
    mode = input("Enter mode of transport (ex: car, train): ") # Enter their mode of transport.
    emissions = get_travel_emissions(distance, mode) # Call the get_travel_emissions function to calculate emissions for the user's trip. 
    print("Estimated emissions:", emissions) # Print the emissions calculation to the user. 