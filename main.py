import os
import datetime
import json
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

if __name__ == "__main__":

    scope = "user-read-recently-played"
    auth_manager = SpotifyOAuth(scope = scope)
    spotify_api = spotipy.Spotify(auth_manager=auth_manager)

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_timestamp = int(yesterday.timestamp()) * 1000

    songs_recently = spotify_api.current_user_recently_played(10,yesterday_timestamp)

    song_name = []
    artist = []
    played_at_list = []
    timestamp = []

    for song in songs_recently["items"]:
        song_name.append(song["track"]["name"])
        artist.append(song["track"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamp.append(song["played_at"][0:10])

    song_dict = {
        "song_name": song_name,
        "artist": artist,
        "played_at": played_at_list,
        "timestamp": timestamp
    }

    song_data_frame = pd.DataFrame(song_dict, columns = song_dict.keys())
    print(song_data_frame)