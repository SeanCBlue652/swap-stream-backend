import requests
import json
import jwt
import cryptography
#ploads = {'Authorization': 'Bearer MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQggN4QX69BA83pO5ODCJVSlrpwgUIToZ1VwT1TaYcOQySgCgYIKoZIzj0DAQehRANCAAQ2o9WU2ecw5jgcaBlr3xD7HL6Vmki3IrKLieCUQyWatYqrMBp9ehBC2Mh+mNy6lJPbCKyXOptInnIUY9g+/lSY'}
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