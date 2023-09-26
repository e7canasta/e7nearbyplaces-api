from fastapi import APIRouter
from pydantic import BaseModel

from slugify import slugify


from e7.ave.places.dash.v1.types import Place
# from e7.ave.places.google.v1.api import get_google_places
from e7.ave.places.google.v1.types import GooglePlace
from e7.ave.places.nearby.v1.api import get_nearby_places
from e7.ave.places.dash.v1.api import get_places

nearby_places_router = APIRouter()


class GetNearbyGPlacesResponse(BaseModel):
    places: list[GooglePlace]
    pass


class GetNearbyPlacesResponse(BaseModel):
    places: list[Place]
    pass


@nearby_places_router.get("/api/v1/nearby_gplaces")
async def GET_nearby_gplaces(lat: float, lng: float, district: str, region: str, subregion: str = None, radius: int = 1200, limit: int = 10, offset: int = 0, sort: str = "distance", country: str = "AR", order: str = "asc", place_type: str = "all", orgin_place_id: str = None) -> GetNearbyGPlacesResponse:
    # places = get_google_places(lat, lng, radius, district, region, subregion, country)
    places = []
    response = GetNearbyGPlacesResponse(places=places)
    return response


@nearby_places_router.get("/api/v1/nearby_places")
async def GET_nearby_places(lat: float, lng: float, district: str, region: str, radius: int, limit: int = 10, offset: int = 0, sort: str = "distance", country: str = "AR", order: str = "asc", place_type: str = "all", orgin_place_id: str = None) -> GetNearbyPlacesResponse:
    places = get_places()
    if district and region:
        district = slugify(district)
        region = slugify(region)
        print(" filtering places by district and region ", district, region)
        fitered_places = []
        for place in places:
            if slugify(place.district) == district and slugify(place.region) == region:
                fitered_places.append(place)
        places = fitered_places
        print(" filtered places ", len(places))

    response = GetNearbyPlacesResponse(places=places)
    return response


class NewNearPlace(BaseModel):
    google_place_id: str
    name: str
    lat: float
    lng: float
    pass


class PostNearbyPlacesRequest(BaseModel):
    places: list[NewNearPlace]
    pass


@nearby_places_router.post("/api/v1/nearby_places")
async def POST_nearby_places(request: PostNearbyPlacesRequest):
    """
    return 200 OK
    """
    return {"status": "ok"}
