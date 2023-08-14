from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mongoengine import connect

from db import create_db
from models import Playground
from models.playground import Location

import json

connect()
app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/searchByLocation/")
def search(location: str):
    matches = Playground.objects(location_id__=Location.objects(name=location).first()).all()
    return JSONResponse(json.loads(matches.to_json()))


@app.get("/playgrounds/{playground_id}")
def get_playground(playground_id: str, q: Union[str, None] = None):
    print(playground_id)
    playground: Playground = Playground.objects(playground_id=playground_id).first()
    if playground:
        return JSONResponse(json.loads(playground.to_json()))
        # return JSONResponse(
        #     {
        #         "playground_id": playground.playground_id,
        #         "name": playground.name,
        #         "location": playground.location_id.name,
        #     }
        # )
    else:
        return JSONResponse(
            {"error": f"Cannot find a playground with id {playground_id}"}
        )
    # return JSONResponse(json.loads(playground.to_json()))
