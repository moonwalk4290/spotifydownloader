from pytube import Search, YouTube
import os
import subprocess

def songSearch(name,artist):
    search = Search(f"{name} - {artist}")
    return search.results[0].watch_url
    

def songDownload(name,artist,playlist_name):
    path = os.path.join(".",playlist_name)
    url = songSearch(name,artist) 
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    down = audio.download(path)
    newPath= os.path.join(path,f"{name}_{artist}.mp4")
    os.rename(down,newPath)
    subprocess.run([
        "ffmpeg",
        "-i",
        newPath,
        os.path.join(path,f"{name}.mp3")
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(newPath)
