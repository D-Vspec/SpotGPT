from LLM import getLLMrecommendations
from SpotifyCommands import *
# from NewPlaylist import makePlaylist
# from AddSongs import addSong
# from SpotifySearch import SpotifySearch

token = getToken()

songList = getLLMrecommendations(input("Enter the recommendations you want: "))
playlist_id, playlist_link = makePlaylist(str(input('Make name: ')), token)

for i in songList:
    if i != '':
        songID = SpotifySearch(i, token)
        print(songID)
        addSong(songID, playlist_id, token)


print('Link to the playlist -> ' + playlist_link)
