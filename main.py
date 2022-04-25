from fastapi import FastAPI
import dao

import test
import json


app = FastAPI() 


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_item(user_id: int):
    return dao.get_userdata()

@app.get("/spotify")
def send_item():
    lib = test.test()
    return lib.playlist_dict