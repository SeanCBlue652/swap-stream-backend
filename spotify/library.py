# library object

import json

import spotipy


class Library:
    def __init__(self, sp: spotipy.Spotify):
        self.sp = sp
        self.user_id = ''
        self.user_name = ''
        self.playlists = None
        self.playlist_dict = dict()
        self.plist_image_url = []
        self.profile_image = ''
    
    def initLib(self):
        print('1')
        sp = self.sp
        print('2')
        self.user_id = str(sp.current_user()['id'])
        print('3')
        self.user_name = str(sp.current_user()['display_name'])
        print('4')
        print(self.user_name)
        print('5')
        self.playlists = sp.current_user_playlists()
        print(self.playlists)
        self.profile_image = sp.current_user()['images'][0]['url']
        # user_id = self.user_id
        # user_name = self.user_name
        playlists = self.playlists
        my_dict = dict()
        user_id = str(sp.current_user()['id'])
        user_name = str(sp.current_user()['display_name'])
        stack = dict()
        the_plist = list()
        stack["name"] = user_name
        stack["service"] = "Spotify"
        stack["id"] = user_id
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                # sp.playlist_add_items(playlist_id=playlist['id'],items=[link], position=None)
                item = sp.playlist_tracks(
                    playlist['id'], fields=None, limit=None, offset=0)
                image = sp.playlist_cover_image(playlist['id'])
                image_entry = image[0]['url']
                plist_name = str(playlist['name'])
                entry = list()

                list_entries = list()
                list_entries.append(stack)
                the_plist.append(entry)
                info_dict = dict()
                info_dict["info"] = list_entries
                info_dict["image"] = image_entry
                info_dict["profile_image"] = self.profile_image
                info_dict["plist_id"] = playlist['id']
                
                entry.append(plist_name)
                entry.append(info_dict)
                for n in range(100):
                    try:
                        song = str(item['items'][n]['track']['name'])
                        artist = str(item['items'][n]['track']
                                     ['artists'][0]['name'])
                        insertion = list()
                        insertion.append(song)
                        insertion.append(artist)
                        entry.append(insertion)
                    except:
                        pass

                my_dict["info"] = list_entries
                my_dict["playlists"] = the_plist
                print(my_dict)
                print("%4d %s %s" %
                      (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None
        self.playlist_dict = my_dict

    def search(self, key):
        return self.playlist_dict[key]

    ''' 
        Queries spotify for song id to add to list
        :param song: list containing song name, song link on spotify, and song artist
    '''

    def searchSpotify(self, song):
        link = song[1]
        name = song[0]
        song_artist = song[2]
        query = None
        query = self.sp.track(link, market=None)
        if query is None:
            query = self.sp.search(
                "track:" + name, limit=300, offset=0, type="track", market=None)
            items = list()
            for each in (query['tracks']['items']):
                blank = each['external_urls']['spotify']
                artist = each['artists'][0]['name']
                print(each['name'] + " by " + artist)
                if artist == song_artist:
                    items.append(blank)
            if len(items) == 0:
                return None
            else:
                return items[0]
        return query['uri']

    def querySpotify(self, s_query):
        query = self.sp.search(s_query, limit=None,
                               offset=0, type="track", market=None)
        items = dict()
        playlist = list()
        playlist.append(s_query)
        playlist.append("Spotify")
        for each in (query['tracks']['items']):
            blank = each['external_urls']['spotify']
            artist = each['artists'][0]['name']
            entry = list()
            entry.append(each['name'])
            entry.append(artist)
            entry.append(blank)
            playlist.append(entry)
        items["query"] = playlist
        return items

    # queries a playlist and adds it with the key, frontend "add" button makes a request to invoke this
    def addToBase(self, plist_name):
        playlist = self.search(plist_name)
        user_id = self.user_id
        user_name = self.user_name

        # Code that invokes the database service and stores the above info

        return playlist, user_id, user_name

    def deliver(self):
        output = list()
        user = dict()
        name = dict()
        user['user_id'] = self.user_id
        name['name'] = self.user_name
        output.append(user)
        output.append(name)
        output.append(self.playlist_dict)
        return json.dumps(self.playlist_dict)

    '''
        Can add playlist

        :param info: the choices the user makes when adding the playlist
        :param plist: the playlist to be added as a list of lists [name, id, artist]
    '''

    def addPlist(self, name: str, plist: list):
        this_list = self.sp.user_playlist_create(
            self.sp.current_user()['id'], name, 
            public=True, 
            collaborative=False, 
            description=''
        )
        items = list()
        for each in plist:
            items.append(each[2])
        for each in plist:
            try:
                link = self.searchSpotify(each[2])
                items.append(link)
            except:
                print(str(each[0]) + " could not be added to target playlist.")
        self.sp.playlist_add_items(
            playlist_id=this_list['id'], items=items, position=None)

    def getToken(self):
        return self.sp.auth_manager.get_access_token(False, False)
