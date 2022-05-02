from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import dao
from spotify import auth_new
from spotify import library


# import test


class Item(BaseModel):
    test: str


class Playlist(BaseModel):
    plist_id: str
    user_id: int
    songs: list
    name: str
    image: str


class CreatePlaylist(BaseModel):
    name: str
    songs: list


class User(BaseModel):
    user_id: int
    user_name: str
    service: str
    pfp: str


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
    return dao.get_user(user_id)


@app.post("/spotify/add")
def add_playlists(item: CreatePlaylist):
    handler.create()
    lib = handler.lib
    # lib.initLib()
    lib.addPlist(item.name, item.songs)
    return item


@app.post("/spotify/add/copy")
def add_playlist_copy(item: CreatePlaylist):
    handler.create()
    lib = handler.lib
    lib.copyPlaylist(item.name, item.songs)
    return item


@app.get("/spotify")
def send_item():
    handler.create()
    sp = handler.sp
    items = dict()
    items['token'] = sp.auth_manager.get_access_token(check_cache=False)
    items['user'] = sp.current_user()['id']
    items['service'] = 'Spotify'
    items['username'] = sp.current_user()['display_name']
    items['pfp'] = sp.current_user()['images'][0]['url']
    return items


@app.get("/spotify/playlists")
def send_playlists():
    lib = handler.lib
    lib.initLib()
    return lib.playlist_dict


@app.post("/post-playlist/")
def post_playlist(playlist: Playlist):
    songs = dict()
    songs['songs'] = playlist.songs
    dao.store_playlist(int(playlist.plist_id), playlist.user_id, songs, playlist.name, playlist.image)
    return playlist


@app.post("/add-user/")
def stuff_2(info: User):
    dao.add_user(info.user_id, info.user_name, info.service, info.pfp)
    return info


@app.get("/getAuth")
def get_auth():
    return {"Token": handler.lib.getToken()}


@app.get("/spotify/{query}")
def query_result(query: str):
    handler.create()
    return handler.lib.querySpotify(query)


@app.get("/all-playlists/")
def all_playlists():
    return dao.get_all_playlists()


@app.get("/search/user/{username}")
def name_result(username: str):
    return dao.get_playlist_by_display_name(username)


@app.get("/search/user/playlist/{user_id}/{plist_id}")
def id_result(user_id: int, plist_id: str):
    return dao.get_playlist_by_id(plist_id, user_id)


@app.get("/search/spotify/{user_id}")
def sp_plist(user_id: int):
    return dao.get_spotify_plist_id(user_id)
