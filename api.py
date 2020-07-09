import json
import requests
from flask import Flask, render_template, request
import json


app = Flask(__name__)




#http://127.0.0.1:5000/makesearch_lyrics?url=https://api.spotify.com/v1/search/?q=Complicated&artist=Mac_Miller
@app.route("/makesearch_lyrics")                   # at the end point /
def make_search():
    token = load_spotify_api()

    url_input  = request.args.get('url', None)
    artist_input  = request.args.get('artist', None)
    artist_name = artist_input.replace("_", " ")
    print(artist_name.rstrip())
    headers = {"Authorization": "Bearer {}".format(token)}
    r = requests.get(url=url_input + "&type=track", headers=headers).json()
    for track in r["tracks"]["items"]:
        curArtist = track["artists"][0]["name"].lower().strip()
        searchArtist = artist_name.lower().strip()
        print(searchArtist)
        if (curArtist == searchArtist):
            print("curArtist: " + curArtist)
            print("searchArtist: " + searchArtist)
            return track
    return "none"




def load_spotify_api():
    with open('keys.json') as f:
        data = json.load(f)
    CLIENT_ID = data['GLOBAL_ID_SPOTIFY']
    CLIENT_SECRET = data['GLOBAL_SECRET_SPOTIFY']
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}

    url='https://accounts.spotify.com/api/token'
    response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET))
    token_raw = json.loads(response.text)
    token = token_raw["access_token"]
    return token


if __name__ == "__main__":
    app.run()

# dictionary = r
# for ele in dictionary:
#     print(ele)
# print(dictionary)
for key in r["tracks"]["items"]:
    print(key["artists"][0]["name"])
# ["tracks"]["items"]
