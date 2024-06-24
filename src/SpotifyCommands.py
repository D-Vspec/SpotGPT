from requests import get, post
import base64
import json

client_id = 'af1afa73842e41cdbeb145d83eb52eb2'
client_secret = 'eaf72736f7614662b4fe66ce2d395140'

redirect_uri = 'http://localhost:8888/callback'

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
    # print(result.content)
    # print('Token is: '+ json_result['access_token'])
    return json_result['access_token']

def makePlaylist(Name, token):
    url = 'https://api.spotify.com/v1/users/newuggzl4u72ucxqqp2qyqka4/playlists'

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
    }
    data = {
        "name": str(Name),
        "description": "ChatGPT playlist",
        "public": False,
    }

    result = post(url, headers=headers, data=json.dumps(data))
    json_result = json.loads(result.content)

    playlist_link = json_result['external_urls']['spotify']

    playlist_id = json_result['id']
    print('Playlist id is: ' + playlist_id)
    return playlist_id, playlist_link

def SpotifySearch(searchterm, token):
    url = 'https://api.spotify.com/v1/search?q='
    url += str(searchterm)
    url += '&type=track'

    headers = {
        "Authorization" : "Bearer " + token
    }

    response = get(url, headers=headers)

    response_json = json.loads(response.content)
    #print(response_json['items'])
    for i in response_json['tracks']['items']:
        return(i['id'])

def addSong(song_id, playlist_id, token):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

    headers = {
        "Authorization" : "Bearer " + token,
        "Content_Type" : "application/json"
    }

    data = {
        "uris" : [f"spotify:track:{song_id}"],
        "position" : 0
    }

    response = post(url, headers=headers, data=json.dumps(data))
