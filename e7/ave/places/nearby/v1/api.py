import requests
import json

"""
   nearby places service methods
"""


def get_nearby_places(lat, lng, radius) -> list:
    """
    get nearby places from google places api
    """
    url = "https://dash.vecinos.com.ar/items/place"
    payload = ""
    response = requests.request("GET", url, data=payload)
    print(response.text)
    return response.json()
#    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&key={PLACES_API_KEY}"
