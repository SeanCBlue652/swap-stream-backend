import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
client_id = '6e0bcc879be24b1c8bff71095368e345'
client_secret = '98602d839f69491681956e0989fbdbb9'
redirect_uri = "http://localhost:4200/"

scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope)) # authorize

playlists = sp.current_user_playlists() # get current user's playlists 
link = "https://open.spotify.com/track/3Qcj8m6FFHhInWjjOrZRom?si=a239da07a46a4eec" #One Piece! sample song
# below loop simply looks through each of the user's playlists and then adds it in
my_dict = dict()
user_id = str(sp.current_user()['uri'])
user_name = str(sp.current_user()['display_name'])
while playlists:
    for i, playlist in enumerate(playlists['items']):
        # sp.playlist_add_items(playlist_id=playlist['id'],items=[link], position=None)
        item = sp.playlist_tracks(playlist['id'], fields=None, limit=50, offset=0)
        entry = list()
        for n in range(5):
            try:
                song = str(item['items'][n]['track']['name'])
                artist = str(item['items'][n]['track']['artists'][0]['name'])
                insertion = f"{song} by {artist}"
                entry.append(insertion)
            except:
                pass
        plist_name = str(playlist['name'])
        key = f"{plist_name}, by {user_name}:{user_id}"
        my_dict[key] = entry
        print("%4d %s %s" %
              (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

print(my_dict) # this dictionary contains the playlist copies with the name of the playlist as the key
# so far, we can retrieve all of the relevant info for swapstream through the above code