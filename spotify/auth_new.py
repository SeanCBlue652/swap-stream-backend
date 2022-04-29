import spotipy
from spotipy.oauth2 import SpotifyOAuth


def run():
    client_id = '6e0bcc879be24b1c8bff71095368e345'
    client_secret = '98602d839f69491681956e0989fbdbb9'
    redirect_uri = "http://localhost:4200/"

    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope))  # authorize
    return sp
