import spotipy
from spotipy.oauth2 import SpotifyOAuth

import spotipy.util as util
import webbrowser
from spotipy import CacheFileHandler
import json



def run():
    client_id = '6e0bcc879be24b1c8bff71095368e345'
    client_secret = '98602d839f69491681956e0989fbdbb9'
    redirect_uri = "http://localhost:8000"

    scope = 'playlist-modify-public'
    handler = CacheFileHandler()
    
    auth_manager = SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope=scope,
                                cache_handler=handler,
                                open_browser=True)
    

    url = auth_manager.get_authorize_url()
    code = auth_manager.get_authorization_code()
    token = auth_manager.get_access_token(code=code, check_cache=False)
    print(code)
    if(token == None):
        webbrowser.open(url)
    sp = spotipy.Spotify(auth_manager=auth_manager)  # authorize
    return sp
