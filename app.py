import json
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("UTF-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "Application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_user_name = os.getenv("USER_NAME")
redirect_uri = os.getenv("REDIRECT_URI")

token = get_token()

scope = 'playlist-modify-public playlist-modify-private user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, requests_timeout=20))


def get_all_songs():   
    songlst = []
    kordus = 0
    
    playlists = sp.current_user_playlists()
    
    for i in playlists["items"]:
        try:  
            results = sp.playlist_tracks(i["id"])
            j = 0
            while (len(results["items"]) > 0):
                for k in results["items"]:
                    songlst.append(k["track"]['uri'])
                    kordus += 1
                j += 1
                results = sp.playlist_tracks(i["id"], offset = j*100)
        except:
            pass
    return songlst



def get_listening_history():
    # Initialize Spotipy
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri, scope='user-read-recently-played'))

    # Fetch your recently played tracks
    history = sp.current_user_recently_played()
    return history



def create_recommendation_playlist(client_id, client_secret, redirect_uri, num_tracks=10, target_seed_track=None):
    
    # If a seed track is provided, use it to generate recommendations
    seed_tracks = [target_seed_track] if target_seed_track else []
    
    # Generate recommendations based on the seed tracks
    
    recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=num_tracks)
    
    # Extract the URIs of the recommended tracks
    
    track_uris = [track['uri'] for track in recommendations['tracks']]

    return track_uris




#fuck yeah
def create_recommendation_based_on_history():
    history = get_listening_history()
    all = get_all_songs()
    
    user_id = sp.current_user()['id']

    playlist_name = "uus soovitus"
    playlist_name = "Your song suggestions"

    playlist = sp.user_playlist_create(user_id, playlist_name, public=True)
    playlist = sp.user_playlist_create(user_id, playlist_name, public=True, description="This suggestion playlist was made with Mihkel Maspanov's Spotify API app")
    for item in history.get("items", []):
        track_name = item.get("track", {}).get("name")
        results = sp.search(q=track_name, type='track')

        # Get the URI of the first track in the search results
        if results['tracks']['items']:
            target_seed_track = results['tracks']['items'][0]['uri']
            laulud = create_recommendation_playlist(client_id, client_secret, redirect_uri, num_tracks=2, target_seed_track=target_seed_track)
            #kontrrolli, et laule ei ole playlistides
            while laulud[0] in all or laulud[1] in all:
                laulud = create_recommendation_playlist(client_id, client_secret, redirect_uri, num_tracks=2, target_seed_track=target_seed_track)
            sp.user_playlist_add_tracks(user_id, playlist["id"], laulud)

create_recommendation_based_on_history()