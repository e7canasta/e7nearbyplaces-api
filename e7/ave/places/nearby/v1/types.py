from pydantic import BaseModel


class Place(BaseModel):
    google_place_id: str
    name: str
    lat: float
    lng: float
    pass