import spotify as sp
import youtube as yt

def songDownload():
    songUrl = input("Enter the song url: ")
    name , artist = sp.getSongName(songUrl)
    yt.songDownload(name, artist, name)
    print(f"Downloaded {name} - {artist} .")


def playlistDownload():
    playlistUrl = input("Enter your playlist url: ")
    (uri,playlistName,songAmount) = sp.getPlaylistInformation(playlistUrl)

    for i in range(songAmount):
        name, artist= sp.getSongNameonPlaylist(uri,i)
        yt.songDownload(name, artist, playlistName)
        print(f"Downloaded {name} - {artist} .")
        
    print(f"Downloaded {songAmount} songs from {playlistName} playlist")


ans = input('''
1- Song Download
2- Playlist Download

Press different key for exit.
''')


if (ans == "1"):
    songDownload()
elif (ans == "2"):
    playlistDownload()
else:
    pass
