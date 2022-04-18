import base64
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
client_id = '6e0bcc879be24b1c8bff71095368e345'
client_secret = '98602d839f69491681956e0989fbdbb9'
redirect_uri = "http://localhost:4200/"

os.environ["SPOTIPY_CLIENT_ID"] = client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
os.environ["SPOTIPY_REDIRECT_URI"] = redirect_uri
scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope)) # authorize

playlists = sp.current_user_playlists() # get current user's playlists 
link = "https://open.spotify.com/track/3Qcj8m6FFHhInWjjOrZRom?si=a239da07a46a4eec" #One Piece! sample song
# below loop simply looks through each of the user's playlists and then adds it in
while playlists:
    for i, playlist in enumerate(playlists['items']):
        # sp.playlist_add_items(playlist_id=playlist['id'],items=[link], position=None)
        print("%4d %s %s" %
              (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
