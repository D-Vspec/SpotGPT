from requests import get
from SpotifyAuth import getToken
import json

token = getToken()

def SpotifySearch(searchterm):
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
        break


