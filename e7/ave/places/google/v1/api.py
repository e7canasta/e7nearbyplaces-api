import requests
import slugify

from e7.ave.places.google.v1.fetch_new_places import fetch_new_place
from e7.ave.places.google.v1.types import map_json_to_google_place, GooglePlace, gplace_loads

GOOGLE_KEY = "AIzaSyBX-H1Lk9ubEY-tLvzgel77UFY2fIf5yzM"


def fetch_google_places(lat: float, lng: float, radius: int = 1200, query: str = "supermercado|carniceria|verduleria|fiambreria") -> list[GooglePlace]:
    gplaces: list[GooglePlace] = []

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


def get_google_places(
        lat: float, lng: float, radius: int = 1200,
        district: str = None, region: str = None, subregion: str = None,
        country: str = None
):
    url = "http://31.220.80.217:8055/items/gplace"
    querystring = {
        "limit": "50",
        "page": "1",
        "filter[_and][1][status][_neq]": "archived"
    }

    if country:
        country = slugify.slugify(country)

    if district:
        district = slugify.slugify(district)

    if region:
        region = slugify.slugify(region)
        print(' [ filtering ] filtering by region ', region)
        querystring["filter[_and][0][_and][0][region][_contains]"] = region

    if subregion:
        subregion = slugify.slugify(subregion)
        print(' [ filtering ] filtering by subregion ', subregion)
        querystring["filter[_and][0][_and][0][subregion][_contains]"] = subregion

    payload = ""
    headers = {"accept": "application/json, text/plain, */*"}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.json)
    data = response.json()["data"]
    gplaces: list[GooglePlace] = []

    if not data:
        print(" sin lugares cercanos.")
        gplaces = fetch_google_places(lat, lng)
        savedPlaces: list[GooglePlace] = []
        for gplace in gplaces:
            gplace.country = country
            gplace.district = district
            gplace.region = region
            gplace.subregion = subregion
            gplace.status = "draft"
            fetch_new_place(gplace)
            # print(" saving gplaces : ", gplace)
            savedPlaces.append(gplace)
        gplaces = savedPlaces
    else:
        for item in data:
            gplace = gplace_loads(item)
            gplaces.append(
                gplace
            )
            # print(" [ gplace ] ", gplace)
    return gplaces
