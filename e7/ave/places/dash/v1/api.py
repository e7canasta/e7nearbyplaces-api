from fastapi import requests

from requests import Response
import requests
from e7.ave.places.dash.v1.types import Place, place_dumps, place_loads


def get_places():
    url = "http://31.220.80.217:8055/items/places"
    payload = ""
    response = requests.request("GET", url, data=payload)
    data = response.json()["data"]
    # map data to model
    places = []
    for item in data:
        place = place_loads(item)
        places.append(
            place
        )
    return places
