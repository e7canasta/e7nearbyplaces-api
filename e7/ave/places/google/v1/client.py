import requests

from e7.ave.places.google.v1.fetch_new_places import fetch_new_place
from e7.ave.places.google.v1.types import GooglePlace, map_json_to_google_place

GOOGLE_KEY = "AIzaSyBX-H1Lk9ubEY-tLvzgel77UFY2fIf5yzM"

def hidrate_google_places(
        lat: float, lng: float, radius: int = 1200,
        district: str = None, region: str = None, subregion: str = None,
        country: str = None
):

    gplaces: list[GooglePlace] = []

    gplaces = fetch_google_places(lat, lng)
    savedPlaces: list[GooglePlace] = []
    for gplace in gplaces:
        fetch_new_place(gplace)
        savedPlaces.append(gplace)
    gplaces = savedPlaces

    return gplaces


def fetch_google_places(lat: float, lng: float, radius: int = 1200, query: str = "supermercado") -> list[GooglePlace]:
    gplaces: list[GooglePlace] = []

    places_types = [
        "supermercado",
        "carniceria",
        "verduleria",
        "almacen|despensa|fiambreria",
        "avicola|panaderia"
    ]

    for place_type in places_types:
        query: str = place_type
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={lat},{lng}&radius={radius}&key={GOOGLE_KEY}"
        payload = ""
        response = requests.request("GET", url, data=payload)
        response = response.json()
        results = response["results"]

        if not results:
            print("sin google places encontrados.")
        else:
            for item in results:
                gplace = map_json_to_google_place(item)
                # print(" [ google place ] ", gplace)
                gplaces.append(gplace)

    return gplaces
