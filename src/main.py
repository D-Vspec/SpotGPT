from LLM import getLLMrecommendations
from SpotifyCommands import *

token = getToken()
playlistName = input("What would you like to name your playlist: ")

songList = getLLMrecommendations(input("Enter the recommendations you want: "))
playlist_id, playlist_link = makePlaylist(playlistName, token)

for index, song in enumerate(songList):
    length = len(songList)
    if song != '':
        songID = SpotifySearch(song, token)
        addSong(songID, playlist_id, token)
        print(f"\rAdded song: {index+1}/{length}", end="")

print('\nLink to the playlist -> ' + playlist_link)
