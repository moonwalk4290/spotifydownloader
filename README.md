# spotifydownloader

## The Goal of the Project
You can download your Spotify favorite song and playlists directly from YouTube. The process is simple, you just need copy your playlist or song url and paste it onto terminal.

---

## Installation
First, make sure about python ,pip and ffmpeg is installed on your system.

Download FFMPEG : https://ffmpeg.org/download.html

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
```


---

## Limitations
- There are not any limitation right now.

---

## Screenshots

![Alt text](https://cdn.discordapp.com/attachments/1117901212117893193/1118600131420360704/image.png)
![Alt text](https://cdn.discordapp.com/attachments/1117901212117893193/1118600757583806555/image.png)

## Common Issues
- There are not any common issue right now.
