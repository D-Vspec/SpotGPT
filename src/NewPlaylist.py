from requests import post
from SpotifyAuth import getToken
import json

token = getToken()
url = 'https://api.spotify.com/v1/users/newuggzl4u72ucxqqp2qyqka4/playlists'

def makePlaylist(Name):
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


