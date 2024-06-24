from flask import Flask, request, jsonify
from flask_cors import CORS
from LLM import getLLMrecommendations
from SpotifyCommands import *

app = Flask(__name__)
CORS(app)


@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    data = request.json
    playlist_name = data.get('playlistName')
    recommendations_input = data.get('description')
    print(recommendations_input)
    if not playlist_name or not recommendations_input:
        return jsonify({'error': 'Missing playlist name or description'}), 400

    token = getToken()
    song_list = getLLMrecommendations(recommendations_input)
    playlist_id, playlist_link = makePlaylist(playlist_name, token)

    for index, song in enumerate(song_list):
        if song:
            song_id = SpotifySearch(song, token)
            addSong(song_id, playlist_id, token)

    return jsonify({'playlistLink': playlist_link})


if __name__ == '__main__':
    app.run(debug=True)
    print("Running app.py as main")