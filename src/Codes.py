import base64
import json
from requests import post

client_id = 'af1afa73842e41cdbeb145d83eb52eb2'
client_secret = 'eaf72736f7614662b4fe66ce2d395140'

redirect_uri = 'http://localhost:8888/callback'
url = "https://accounts.spotify.com/api/token"
code_url = f'https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri=http://localhost:8888/callback&show_dialog=true&scope=playlist-modify-private playlist-modify-public playlist-read-private playlist-read-collaborative ugc-image-upload'
code = input('code\n')


def getCode():
    auth_string = client_id + ':' + client_secret
    auth_64 = auth_string.encode("utf-8")
    auth_64_encoded = str(base64.b64encode(auth_64), "utf-8")

    headers = {
        "Authorization": "Basic " + auth_64_encoded,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri
    }
    response = post(url, headers=headers, data=body)
    print(response.content)
    response_json = json.loads(response.content)
    token = response_json["refresh_token"]
    return token
