import openai
from NewPlaylist import makePlaylist
from AddSongs import addSong
from SpotifySearch import SpotifySearch

openai.api_key = "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"

Output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me a list of 10 k-pop songs"}
    ]
)

Output_Reply_1 = Output.choices[0].message.content
print(Output_Reply_1)

playlist_id, playlist_link = makePlaylist(str(input('Make name: ')))
Reply_split = Output_Reply_1.splitlines()

for i in Reply_split:
    if i != '':
        songID = SpotifySearch(i)
        print(songID)
        addSong(songID, playlist_id)


print('Link to the playlist -> ' + playlist_link)
