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


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

#search for artist and get top tracks
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    #otsin artisti nime ja otsin ainult ühte limitiga, muidu tuleb liiga palju
    query = f"?q={artist_name}&type=artist&limit=1"
    
    query_url = url + query
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists")
        return None
    return json_result[0]


def get_songs_by_artist(token, artist_id):
    #lõpus annad riigi kust otsid top tracke
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


def get_auth(redirect_uri, client_id, client_secret):
    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope='user-library-read user-library-modify playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public')

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print("Open the following URL in your browser:")
        print(auth_url)
        response = input("Enter the URL you were redirected to: ")
    
        token_info = sp_oauth.get_access_token(response)

    if token_info:
        token = token_info['access_token']

def print_playlists(client_id, client_secret, redirect_uri):
    # Scope defines the permissions you need
    scope = 'playlist-read-private playlist-read-collaborative'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

    # Now you have a Spotify instance with access to your playlists

    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        print(playlist['name'])


def get_playlist_tracks(playlist_name):
    scope = 'playlist-read-private playlist-read-collaborative'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
    playlists = sp.current_user_playlists()
    playlist_id = None
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
            break
    # Check if the playlist was found
    if playlist_id:
        # Retrieve the tracks within the playlist
        playlist_tracks = sp.playlist_tracks(playlist_id)

        # Print the track names
        for track in playlist_tracks['items']:
            print(track['track']['name'])
    else:
        print(f"Playlist '{playlist_name}' not found.")


def get_listening_history():
    # Initialize Spotipy
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id', client_secret='your_client_secret', redirect_uri='http://localhost:3000/callback', scope='user-read-recently-played'))

    # Fetch your recently played tracks
    history = sp.current_user_recently_played()
    return history


def create_recommendation_playlist(client_id, client_secret, redirect_uri, playlist_name, num_tracks=10, target_seed_track=None):
    # Scope defines the permissions your app needs
    scope = 'playlist-modify-public playlist-modify-private user-library-read'

    # Initialize the Spotify client with authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

    # Get the user's ID
    user_id = sp.current_user()['id']

    # Create a new playlist
    playlist = sp.user_playlist_create(user_id, playlist_name, public=True)

    # If a seed track is provided, use it to generate recommendations
    seed_tracks = [target_seed_track] if target_seed_track else []
    
    # Generate recommendations based on the seed tracks
    recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=num_tracks)

    # Extract the URIs of the recommended tracks
    track_uris = [track['uri'] for track in recommendations['tracks']]

    # Add the recommended tracks to the newly created playlist
    sp.user_playlist_add_tracks(user_id, playlist['id'], track_uris)

    print(f"Created a playlist '{playlist_name}' with {len(track_uris)} recommended tracks.")



#TÖÖTAB
#target_seed_track = 'spotify:track:YOUR_SEED_TRACK_URI'
target_seed_track = 'spotify:track:4rXLjWdF2ZZpXCVTfWcshS'

#create_recommendation_playlist(client_id, client_secret, redirect_uri, 'My Recommended Playlist', target_seed_track=target_seed_track)

#MUST FIX

def create_recommendation_playlist_from_history(client_id, client_secret, redirect_uri, playlist_name, num_tracks=10):
    # Scope defines the permissions your app needs
    scope = 'playlist-modify-public playlist-modify-private user-library-read user-read-recently-played'

    try:
        # Initialize the Spotify client with authentication
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

        # Get the user's ID
        user_id = sp.current_user()['id']

        # Fetch the user's recently played tracks
        history = sp.current_user_recently_played()
        seed_tracks = [item['track']['uri'] for item in history['items']]

        # Create a new private playlist
        playlist = sp.user_playlist_create(user_id, playlist_name, public=False)

        # Generate recommendations based on your listening history (seed tracks)
        recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=30)

        # Extract the URIs of the recommended tracks
        track_uris = [track['uri'] for track in recommendations['tracks']]

        # Add the recommended tracks to the newly created playlist
        sp.user_playlist_add_tracks(user_id, playlist['id'], track_uris)

        print(f"Created a recommended playlist '{playlist_name}' with {len(track_uris)} tracks from your listening history.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

#create_recommendation_playlist_from_history(client_id, client_secret, redirect_uri, "recommended playlist", num_tracks=10)

def create_recommendation_based_based_on_history():
    history = get_listening_history()
    print(history["items"])
create_recommendation_based_based_on_history()

#result = search_for_artist(token, "eminem")
#artisti nimi
#print(result["name"])

#artisti is
#artist_id = result["id"]
#songs = get_songs_by_artist(token, artist_id)

#for idx, song in enumerate(songs):
    #print(f"{idx + 1}. {song['name']}")


#get_auth(redierct_uri, client_id, client_secret)


#print_playlists(client_id, client_secret, redirect_uri)

#get_playlist_tracks("Maskita ei teeks")


