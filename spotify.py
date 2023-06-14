import requests

ID = ""
SECRET = ""

'''

Get your client ID and client secret from : https://developer.spotify.com/dashboard/

'''

def getToken():
    result = requests.post(
    "https://accounts.spotify.com/api/token",
     headers= {"content-type": "application/x-www-form-urlencoded"},
     data= f"grant_type=client_credentials&client_id={ID}&client_secret={SECRET}"
                    )
    return result.json()["access_token"]

def getPlaylistInformation(url):
    uri = url[34:56]
    token = getToken()
    result = requests.get(
        f'https://api.spotify.com/v1/playlists/{uri}',
        headers= {"authorization":f"Bearer {token}"},
    )
    playlistName = result.json()["name"]
    songAmount = result.json()["tracks"]["total"]
    return uri,playlistName,songAmount


def getSongName(uri,index):
    token = getToken()
    result = requests.get(
        f'https://api.spotify.com/v1/playlists/{uri}',
        headers= {"authorization":f"Bearer {token}"},
    )
    trackName = result.json()["tracks"]["items"][index]["track"]["name"]
    artist = result.json()["tracks"]["items"][index]["track"]["artists"][0]["name"]
    return trackName, artist
