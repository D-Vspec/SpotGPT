import LLM
from NewPlaylist import makePlaylist
from AddSongs import addSong
from SpotifySearch import SpotifySearch

songList = input("Enter the recommendations you want")

playlist_id, playlist_link = makePlaylist(str(input('Make name: ')))

for i in songList:
    if i != '':
        songID = SpotifySearch(i)
        print(songID)
        addSong(songID, playlist_id)


print('Link to the playlist -> ' + playlist_link)
