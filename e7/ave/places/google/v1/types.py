import json
from typing import List, Optional

from pydantic import BaseModel


def parse_address(full_address):
    # Dividir la dirección en partes por comas
    address_parts = full_address.split(",")

    if len(address_parts) >= 1:
        # Obtener la primera parte de la dirección y eliminar espacios en blanco
        first_part = address_parts[0].strip()

        # Dividir la primera parte en palabras
        words = first_part.split()

        if len(words) >= 2 and words[-1].isdigit():
            # Si la última palabra es un número, considerarlo como número de calle
            street_name = " ".join(words[:-1])  # El nombre de la calle es todo menos la última palabra
            street_number = words[-1]  # El número de la calle es la última palabra
        else:
            # No se encontró un número de calle, establecer número de calle en 0
            street_name = first_part
            street_number = "0"

        return [street_name, street_number]
    else:
        # Manejar el caso en el que no hay partes en la dirección
        return [None, None]


class GeoPoint(BaseModel):
    type: str
    coordinates: List[float]


class GooglePlace(BaseModel):
    status: str
    name: Optional[str]
    placeId: Optional[str]
    reference: Optional[str]
    geopoint: GeoPoint
    address: Optional[str]
    street: Optional[str]
    streetNumber: Optional[int]
    district: Optional[str]
    region: Optional[str]
    subregion: Optional[str]
    country: Optional[str]
    photoRef: Optional[str]
    photo: Optional[str]
#    labels: Optional[List[str]]


def map_json_to_google_place(data) -> GooglePlace:
    # print("[ data ]", data)
    address = data["formatted_address"] # "Av. Directorio 5425, C1440 ASG, Buenos Aires, Argentina"
    street, streetNumber = parse_address(address)
    # print(" [ lng ] -> ",  data["geometry"]["location"]["lng"])

    google_place = GooglePlace(
        status="draft",
        name=data["name"],
        placeId=data["place_id"],
        reference=data["reference"],
        geopoint=GeoPoint(type="Point",
                          coordinates=[
                              data["geometry"]["location"]["lng"],
                              data["geometry"]["location"]["lat"]
                          ]),
        address=address,
        street=street,
        streetNumber=streetNumber,
        district=None,  # Define esto según tus datos si es necesario
        region=None,  # Define esto según tus datos si es necesario
        subregion=None,
        country=None,  # Define esto según tus datos si es necesario
        photoRef=None,  # Define esto según tus datos si es necesario
        photo=None,  # Define esto según tus datos si es necesario
        labels=data["types"]
    )
    return google_place


def gplace_loads(data_dict: str) -> GooglePlace:
    data_dict["placeId"] = data_dict["place_id"]
    data_dict["photo"] = data_dict["photo"]
    data_dict["streetNumber"] = data_dict["street_number"]
    data_dict["reference"] = ""
    data_dict["district"] = ""
    data_dict["photoRef"] = ""
    data_dict["country"] = ""

    print("[001] ...................................")
    print(data_dict)
    place_obj = GooglePlace(**data_dict)
    return place_obj


if __name__ == '__main__':

    sample_data =  {'business_status': 'OPERATIONAL', 'formatted_address': 'Av. Directorio 5425, C1440 ASG, Buenos Aires, Argentina', 'geometry': {'location': {'lat': -34.6536134, 'lng': -58.4945436}, 'viewport': {'northeast': {'lat': -34.65230127010727, 'lng': -58.49314687010728}, 'southwest': {'lat': -34.65500092989272, 'lng': -58.49584652989272}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png', 'icon_background_color': '#4B96F3', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/shoppingcart_pinlet', 'name': 'Supermercado carnicería verdulería', 'opening_hours': {'open_now': True}, 'photos': [{'height': 1080, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/103247622280979675800">Funren You</a>'], 'photo_reference': 'ATJ83zjO-LZac4FjpH_or04QOmU_T0XkftCcPMrbfiN358uNyNF-fOmKu9HNoKNahK_tCMvNsRazVJsYYyiCEdDhIawexaiIAhJ0NZPuYu2JccAUBfdeNlXaw0ZdipgVy9sgy5IcfRrkQp1F8LC7uEX9ib4iKBHDEfLM4crx1ciAR7qIeCb4', 'width': 1920}], 'place_id': 'ChIJBYPSTuvJvJURX_kAO6P0Qwc', 'plus_code': {'compound_code': '8GW4+H5 Buenos Aires', 'global_code': '48Q38GW4+H5'}, 'rating': 4.7, 'reference': 'ChIJBYPSTuvJvJURX_kAO6P0Qwc', 'types': ['supermarket', 'grocery_or_supermarket', 'food', 'point_of_interest', 'store', 'establishment'], 'user_ratings_total': 12}
    gplace= map_json_to_google_place(sample_data)
    print("...............................")
    print(gplace)

