from pytube import YouTube , Search
import os

def songSearch(name,artist):
    search = Search(f"{name} - {artist}")
    return search.results[0].watch_url
    


def songDownload(name,artist,playlist_name):
    url = songSearch(name,artist)
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    path = os.path.join(".",playlist_name)
    video.download(output_path=path)
