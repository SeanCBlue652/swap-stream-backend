import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import CacheFileHandler
import spotipy.util as util
import json
import webbrowser

scope = 'playlist-modify-public'

client_id = '6e0bcc879be24b1c8bff71095368e345'
client_secret = '98602d839f69491681956e0989fbdbb9'
redirect_uri = "http://localhost:8000"

username = 1225933126
# os.remove(f".cache-{username}")
# token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope=scope)
auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope=scope,
                            open_browser=True)
url = auth_manager.get_authorize_url()
# webbrowser.open(url)
code = auth_manager.get_authorization_code()
token = auth_manager.get_access_token(code=code,as_dict=False,check_cache=False)
print(code)
print(token)