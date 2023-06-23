import base64
import json
from requests import post

client_id = 'af1afa73842e41cdbeb145d83eb52eb2'
client_secret = 'eaf72736f7614662b4fe66ce2d395140'
redirect_uri = 'http://localhost:8888/callback'
url = "https://accounts.spotify.com/authorize"

def getToken():

    auth_string = client_id + ':' + client_secret
    auth_64 = auth_string.encode("utf-8")
    auth_64_encoded = str(base64.b64encode(auth_64), "utf-8")
    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_64_encoded,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "refresh_token",
        'refresh_token': "AQDazHuo85IzH8GOIz6Ex_lkkVv7q-_XGyq6V-PBmgr44y27R6zmHoS9ukDle4bV-WUoDFr47nAGbiBspdwxe4pVzterIbWKi0NHlWEICt29WA5TYcrkEvgbqSkDdqRyI4I"
    }
    result = post(url, headers=headers, data=data)

    json_result = json.loads(result.content)
    #print(result.content)
    #print('Token is: '+ json_result['access_token'])
    return json_result['access_token']