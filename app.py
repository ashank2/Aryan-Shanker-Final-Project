#-------------------------------
# Front-End Web App Development
#-------------------------------

from flask import Flask, render_template, request

# Import Backend API Functions:
from api_integrations import geocode_location, get_travel_emissions

# Import Main ML Function (recommend_greener_mode) For The Landing Page:
from ml_functions import recommend_greener_mode

# Other ML Functions will be integrated in future web app updates as additional pages or dashboards.
# For now, the first version, integrating only one ML Function: (recommend_greener_mode). 
# summarize_user_trips, 
# plot_emissions_over_time, 
# predict_mode, 
# analyze_user_commute_feedback, 
# save_user_trips_to_csv, 
# load_user_trips_from_csv


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Main route for the landing page.
    Handles the GET (showing of the form) and POST (for processing user input).
    """
    # AI was used for debugging purposes on line 34, line 41, line 49, lines 52 to 59.
    # and was used as a help to create result message for the user - lines 62 to 68.
    result = None # Placeholder for result message.

    if request.method == "POST":
        # Get user input from the form:
        location = request.form.get("location") # Location input.
        distance = request.form.get("distance") # Distance travelled input.
        mode = request.form.get("mode") # Mode of transport input. 

        # Check if all fields are filled appropriately by the user:
        if location and distance and mode:
            # Geocode the location inputted by the user, using Mapbox API:
            coords = geocode_location(location) # Return coordinates. 

            # Calculate emissions using Climatiq API:
            emissions = get_travel_emissions(float(distance), mode) 

            # Get a greener recommendation using recommend_greener_mode ML Function:
            greener_mode = recommend_greener_mode(float(distance), mode)

            # Handle Emissions Results For Display To Users:
            if emissions is None:
                emissions_display = "<i>Could not calculate emissions for this trip.</i>"
            
            elif emissions == 0:
                emissions_display = "Zero emissions!"
            else:
                emissions_display = f"{emissions:.2f} kg CO2"

            #Build the result message for the user:
            result = (
                f"<b>Starting Location:</b> {location} <br>"
                f"<b>Coordinates:</b> {coords} <br>"
                f"<b>Distance:</b> {distance} km <br>"
                f"<b>Mode:</b> {mode.capitalize()} <br>"
                f"<b>Estimated Emissions:</b> {emissions_display} <br>"
                f"<b>Greener Recommendation:</b> {greener_mode}"
            )
        else:
        # If any field is missing, show an error message:
            result = "Please fill in all fields!"

# Render the index.html template, passing the result through it.
    return render_template("index.html", result=result)

if __name__ == "__main__":
    # To start the Flask development server. 
    app.run(debug=True)
