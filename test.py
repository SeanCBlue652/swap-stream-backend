from spotify import library
from spotify import auth_new

query_list = list()

def test():
    new_sp = auth_new.run()
    lib = library.Library(new_sp)
    return lib

def newTest():
    lib = test()
    result = lib.findSongByNameAndArtist('Knife Talk', 'Drake')
    # sp = auth_new.run(scope='user-modify-playback-state')
    query_list.append(result)
    result = lib.findSongByNameAndArtist('I Am A God', 'Kanye West')
    query_list.append(result)
    print(result)
    lib.addPlistCopy("Test Playlist", query_list)

def secondTest():
    lib = test()
    items = [
        ['Knife Talk', 'Drake'],
        ['I Am A God', 'Kanye'],
        ['Monster', 'Kanye'],
        ['Starboy', 'Weeknd']
    ]
    lib.copyPlaylist('Test 2', items)

secondTest()