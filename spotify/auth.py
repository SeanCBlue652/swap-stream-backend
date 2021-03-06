
import requests

import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import CacheFileHandler
import spotipy.util as util
import json


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


client_id = '6e0bcc879be24b1c8bff71095368e345'
client_secret = '98602d839f69491681956e0989fbdbb9'
redirect_uri = "http://localhost:4200/"

# auth_manager= SpotifyClientCredentials
scope = 'playlist-modify-public'
item = CacheFileHandler()
print(item.get_cached_token())
username = 1225933126
# os.remove(f".cache-{username}")
token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret,redirect_uri=redirect_uri, scope=scope)

auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope=scope,
                            open_browser=True)
print(auth_manager)

sp = spotipy.Spotify(auth_manager=auth_manager)  # authorize
# sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.current_user_playlists()  # get current user's playlists
link = "https://open.spotify.com/track/3Qcj8m6FFHhInWjjOrZRom?si=a239da07a46a4eec"  # One Piece! sample song
# below loop simply looks through each of the user's playlists and then adds it in
my_dict = dict()
user_id = str(sp.current_user()['id'])
user_name = str(sp.current_user()['display_name'])
stack = dict()
the_plist = list()
stack["name"] = user_name
stack["service"] = "Spotify"
stack["id"] = user_id
print(user_id)
print(sp.current_user()['images'][0]['url'])
while playlists:
    for i, playlist in enumerate(playlists['items']):
        # sp.playlist_add_items(playlist_id=playlist['id'],items=[link], position=None)
        item = sp.playlist_tracks(playlist['id'], fields=None, limit=None, offset=0)

        image = sp.playlist_cover_image(playlist['id'])
        # print(image[0]['url'])
        
        plist_name = str(playlist['name'])
        entry = list()
        entry.append(plist_name)
        for n in range(20):
            try:
                song = str(item['items'][n]['track']['name'])
                artist = str(item['items'][n]['track']['artists'][0]['name'])
                # insertion = f"{song} by {artist}"
                insertion = list()
                insertion.append(song)
                insertion.append(artist)
                entry.append(insertion)
            except:
                pass

        list_entries = list()
        list_entries.append(stack)
        the_plist.append(entry)
        key = f"{plist_name}"
        my_dict["info"] = list_entries
        my_dict["playlists"] = the_plist
        # print(my_dict)
        # print("%4d %s %s" %
        # (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

# this dictionary contains the playlist copies with the name of the playlist as the key
# so far, we can retrieve all of the relevant info for swapstream through the above code
# print(json.dumps(my_dict))
# print(sp.current_user()['id'])
query = sp.track(link, market=None)
# print(query['uri'])
# print(query)
# pint = sp.user_playlist_create(sp.current_user()['id'], "Same Old", True, False, None)
# sp.playlist_add_items(playlist_id=pint['id'],items=[query['uri']], position=None)

query = sp.search("track:Brown Boy Summer", limit=None, offset=0, type="track", market=None)

items = list()
for each in (query['tracks']['items']):
    blank = each['external_urls']['spotify']
    artist = each['artists'][0]['name']
    print(each['name'] + " by " + artist)
    if artist == "Moonshot18":
        items.append(blank)
print(items)
# sp.playlist_add_items(playlist_id=pint['id'], items=items, position=None)

# sp.auth_manager.refresh_access_token()
token = sp.auth_manager.get_access_token(False, False)
print(token)
