# library object
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import json

class Library:
    def __init__(self, sp):
        self.sp = sp
        self.user_id = str(sp.current_user()['uri'])
        self.user_name = str(sp.current_user()['display_name'])
        self.playlists = sp.current_user_playlists()
        my_dict = dict()
        # user_id = self.user_id
        # user_name = self.user_name
        playlists = self.playlists
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                # sp.playlist_add_items(playlist_id=playlist['id'],items=[link], position=None)
                item = sp.playlist_tracks(playlist['id'], fields=None, limit=None, offset=0)
                entry = list()
                for n in range(100):
                    try:
                        song = str(item['items'][n]['track']['name'])
                        # artist = str(item['items'][n]['track']['artists'][0]['name'])
                        # insertion = f"{song} by {artist}"
                        insertion = song
                        entry.append(insertion)
                    except:
                        pass
                plist_name = str(playlist['name'])
                # key = f"{plist_name}, by {user_name}:{user_id}"
                key = plist_name
                my_dict[key] = entry
                print("%4d %s %s" %
                    (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None
        self.playlist_dict = my_dict
    
    def search(self, key):
        return self.playlist_dict[key]

    def addToBase(self, plist_name): # queries a playlist and adds it with the key, frontend "add" button makes a request to invoke this
        playlist = self.search(plist_name)
        user_id = self.user_id
        user_name = self.user_name

        # Code that invokes the database service and stores the above info

        return (playlist, user_id, user_name)

    def deliver(self):
        output = list()
        user = dict()
        name = dict()
        user['user_id'] = self.user_id 
        name['name'] = self.user_name
        output.append(user)
        output.append(name)
        output.append(self.playlist_dict)
        return json.dumps(output)