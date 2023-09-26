import requests

from e7.ave.places.google.v1.types import GooglePlace

PLACE_URL = "http://31.220.80.217:8055/items/glaces"


def fetch_new_place(newPlace: GooglePlace):
    placeIn = {
        "name": newPlace.name,
        #"reference": newPlace.reference,
        "place_id": newPlace.placeId,
        "status": newPlace.status,
        "geopoint": {
            "type": "Point",
            "coordinates": [
                newPlace.geopoint.coordinates[0],
                newPlace.geopoint.coordinates[1]
            ]
        },
        "address": newPlace.address,
        "street": newPlace.street,
        "street_number": newPlace.streetNumber,
        #"district": newPlace.district,
        #"region": newPlace.region,
        #"country": newPlace.country,
        #"photo_reference": newPlace.photoRef
    }

    stored_place = None
    try:
        response = requests.post(PLACE_URL, json=placeIn)
        response = response.json()
        # print(response)
        data = response["data"]
        stored_place = {
            **newPlace
        }
    except Exception as error:
        print("Error:", error)

    return stored_place


# Ejemplo de uso:
# new_place = {
#     "status": "published",
#     "name": "Ejemplo Lugar",
#     "coords": {
#         "longitude": 123.45,
#         "latitude": 67.89
#     },
#     # Añade el resto de los campos aquí
# }


# stored_place = fetch_new_place(new_place)
# if stored_place:
#     print("Lugar almacenado:", stored_place)