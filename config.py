#---------------------------------------
# Configuration Of Environment Variables
#---------------------------------------

import os
from dotenv import load_dotenv # To help load .env files.

# Load environment variables from .env file (containing the API Keys)
load_dotenv()

# Retrieve API keys from environment variables:
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
CLIMATIQ_API_KEY = os.getenv("CLIMATIQ_API_KEY")

# For debugging purposes (can uncomment the following lines for checks):
# print("MAPBOX_TOKEN", MAPBOX_TOKEN)
# print("CLIMATIQ_API_KEY", CLIMATIQ_API_KEY)
