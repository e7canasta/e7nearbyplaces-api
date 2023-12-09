from pydantic import BaseModel
from slugify import slugify

from fastapi import APIRouter

hooks_places_router = APIRouter()


class CreateRequest(BaseModel):
    event: str
    accountability: dict
    payload: dict
    key: str
    collection: str


class UpdateRequest(BaseModel):
    event: str
    accountability: dict
    payload: dict
    keys: list
    collection: str


@hooks_places_router.post("/api/v1/hooks/places/create")
async def POST_hooks_places_create(request: CreateRequest):
    print(request)
    return {
        "status": "OK",
        "request": request
    }


@hooks_places_router.post("/api/v1/hooks/places/update")
async def POST_hooks_places_update(request: UpdateRequest):
    print(request)
    return {
        "status": "OK",
        "request": request
    }
