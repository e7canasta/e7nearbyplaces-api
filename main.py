from fastapi import FastAPI

from app.web.routes.nearby_places import nearby_places_router

app = FastAPI()

app.include_router(nearby_places_router)



@app.get("/")
async def root():
    return { "message": "hola vecino" }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run("app.web:app", host="192.168.0.14", port=8000, log_level="info")