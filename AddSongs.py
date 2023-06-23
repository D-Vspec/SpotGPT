from requests import post
from SpotifyAuth import getToken
import json

token = getToken()

def addSong(song_id, playlist_id):
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
    print(response.content)

