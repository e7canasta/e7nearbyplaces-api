import requests
import slugify

from e7.ave.places.google.v1.types import GooglePlace, gplace_loads



def get_gplaces(
        lat: float, lng: float, radius: int = 1200,
        district: str = None, region: str = None, subregion: str = None,
        country: str = None
):

    url = "http://31.220.80.217:8055/items/glaces"

    querystring = {
        "limit": "50",
        "page": "1",
        "filter[_and][1][status][_neq]": "archived"
    }

#     if country:
#         country = slugify.slugify(country)
#
#     if district:
#         district = slugify.slugify(district)
#
#     if region:
#         region = slugify.slugify(region)
#         print(' [ filtering ] filtering by region ', region)
#         querystring["filter[_and][0][_and][0][region][_contains]"] = region
#
#     if subregion:
#         subregion = slugify.slugify(subregion)
#         print(' [ filtering ] filtering by subregion ', subregion)
#         querystring["filter[_and][0][_and][0][subregion][_contains]"] = subregion

    headers = {"accept": "application/json, text/plain, */*"}
    payload = ""

    print(".....................................")
    response = requests.request("GET", url, data=payload)
    # response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.json)
    data = response.json()["data"]
    gplaces: list[GooglePlace] = []

    if not data:
        print(" sin lugares cercanos.")
        return gplaces
    else:
        for item in data:
            gplace = gplace_loads(item)
            gplaces.append(
                gplace
            )
    return gplaces
