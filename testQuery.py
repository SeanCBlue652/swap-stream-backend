import dao
import json

def testAddUser():
    for n in range(1734334,1734337):
        dao.add_user(n, "'Stone'", "'Spotify'")

def testStorePlaylists():
    item = ['Best I Ever Had', 'Drake']
    songs = dict()
    songs['songs'] = item
    dao.store_playlist(1265, 1225933126, songs, 'Test', 'im')

# testAddUser()
# print(dao.get_test_data())
# testStorePlaylists()
# items = dao.get_playlist_by_id(1265, 1225933126)
# items = dao.get_user(1225933126)
items = dao.get_playlist_by_display_name('Suhaib')
print(items)