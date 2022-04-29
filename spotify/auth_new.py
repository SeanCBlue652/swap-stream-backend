import spotipy
from spotipy.oauth2 import SpotifyOAuth


def run():
    client_id = '73484c021b8545c29225c24a1d8ee5e0'
    client_secret = '91555a75e07c47ee816e39db529b0c10'
    redirect_uri = "http://localhost:4200/"

    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope))  # authorize
    return sp
