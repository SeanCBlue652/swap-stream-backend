from fastapi import FastAPI
import dao
import test
import json
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI() 

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

lib = test.test()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/p")
def stuff():
    return dao.get_test_data()

@app.get("/users/{user_id}")
def read_item(user_id: int):
    return dao.get_userdata()

@app.get("/spotify")
def send_item():
    lib.initLib()
    return lib.playlist_dict

@app.get("/spotify/{query}")
def query_result(query: str):
    return lib.querySpotify(query)