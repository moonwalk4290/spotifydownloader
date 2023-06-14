# spotifydownloader

## The Goal of the Project
You can download your Spotify playlists directly from YouTube. The process is simple, you just need copy your playlist url and paste it onto terminal.

---

## Installation
First, make sure about python ,pip and ffmpeg is installed on your system.

FFMPEG : https://ffmpeg.org/download.html

Than, go to the terminal and:
```
$ git clone https://github.com/moonwalk4290/spotifydownloader.git
$ cd spotifydownloader/
$ pip install -r requirements.txt
```

If thats your first time using this project, you must get client ID and client secret from Spotify.
To do this:

1) Go to the https://developer.spotify.com/dashboard/ page. (If you don't have a spotify account, you have to create one.)
2) Click "New App" button on the right side and enter your app information:<br>
  App name:        (your app name) <br>
  App description: (your app description) <br>
  Redirect URIs:   ("spotify.com") <br>
3) Go to your new created app and click "Settings" button.
4) Click "View client secret" and you should see your ID and Secret.
5) Copy them, open "spotify.py" file that you installed and paste them on ID and SECRET fields.
  
You are now ready to use spotifydownloader. 

---

## Usage

```
$ cd spotifydownloader/           => Or just go to where you installed this tool.
$ python main.py

Enter your playlist url: ("Enter your spotify playlist url")
```

It automatically downloads your songs.

---

## Limitations
- It can only download playlists right now, it can't download just one song.
- It gives an error when you try to download a playlist includes podcast (some songs in your playlist maybe podcasts).

---

## Screenshots

![Alt text](https://cdn.discordapp.com/attachments/1117901212117893193/1118404759645339658/image.png)
