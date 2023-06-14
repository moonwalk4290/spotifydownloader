import spotify as sp
import youtube as yt

playlistUrl = input("Enter your playlist url: ")
(uri,playlistName,songAmount) = sp.getPlaylistInformation(playlistUrl)

for i in range(songAmount):
    name, artist= sp.getSongName(uri,i)
    name = yt.songDownload(name, artist, playlistName)
    
print(f"Downloaded {songAmount} songs from {playlistName} playlist")
