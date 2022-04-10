import requests
import json
import jwt
import cryptography
#ploads = {'Authorization': 'Bearer '}
#r = requests.get('https://api.music.apple.com/v1/me/library/playlists')
#print(r.headers)
#print(r.text)
#print(r.json())

import applemusicpy

secret_key = ''
key_id = '74G4697BU4'
team_id = 'QTM38LJQ3P'

am = applemusicpy.AppleMusic(secret_key, key_id, team_id)
results = am.search('travis scott', types=['albums'], limit=5)

for item in results['results']['albums']['data']:
    print(item['attributes']['name'])