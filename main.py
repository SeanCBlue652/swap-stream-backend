from fastapi import FastAPI
import dao
# import test
import json
from fastapi.middleware.cors import CORSMiddleware
from spotify import library
from spotify import auth_new

class Handler:
    def __init__(self):
        self.sp = None
        self.lib = None
    def create(self):    
        self.sp = auth_new.run()
        self.lib = library.Library(self.sp)

handler = Handler()
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
    handler.create()
    sp = handler.sp
    return sp.auth_manager.get_access_token(check_cache=False)

@app.get("/spotify/playlists")
def send_playlists():
    lib = handler.lib
    lib.initLib()
    return lib.playlist_dict

@app.post("/add-user/")
def stuff_2(info):
    dao.add_user(info.user_id, info.user_name, info.service)

@app.get("/getAuth")
def get_auth():
    return {"Token":handler.lib.getToken()}

@app.get("/spotify/{query}")
def query_result(query: str):
    return handler.lib.querySpotify(query)