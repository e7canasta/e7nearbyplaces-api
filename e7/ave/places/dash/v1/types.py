import json

from pydantic import BaseModel
from typing import List, Optional


class GeoPoint(BaseModel):
    type: str
    coordinates: List[float]


class Place(BaseModel):
    id: str
    status: str
    date_created: str
    date_updated: str
    geopoint: GeoPoint
    address: Optional[str]
    city: Optional[str]
    district: Optional[str]
    region: Optional[str]
    subregion: Optional[str]
    postal_code: Optional[str]
    street: Optional[str]
    street_number: Optional[int]
    country: Optional[str]
    name: Optional[str]
    country_code: Optional[str]
    district: Optional[str]
    city: Optional[str]
    region: Optional[str]
    subregion: Optional[str]
    country: Optional[str]
    alerted: Optional[bool]
    photo: Optional[str]


def place_loads(data_dict: str) -> Place:
    print(data_dict)
    data_dict["district"] = data_dict["raw_district"]
    data_dict["city"] = data_dict["raw_city"]
    data_dict["region"] = data_dict["raw_region"]
    data_dict["subregion"] = data_dict["raw_subregion"]
    data_dict["country"] = ""  # data_dict["raw_country"]
    # geo_point_obj = GeoPoint(**data_dict["geopoint"])
    place_obj = Place(**data_dict)
    return place_obj


def place_dumps(place: Place) -> str:
    return json.dumps(place.dict(), indent=4)
