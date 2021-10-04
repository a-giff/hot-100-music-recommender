#!/usr/bin/env python
# coding: utf-8

# # Import Statements

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances, cosine_distances, euclidean_distances
from spotifyClient import SpotifyAPI

pd.set_option('display.max_columns', None)

class RecommendSong:
    col_name = [
        'song', 'album', 'artist', 'popularity', 'track_id',
       'track_explicit', 'danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_ms', 'time_signature', 'num_samples',
       'duration', 'end_of_fade_in', 'start_of_fade_out', 'tempo_confidence',
       'time_signature_confidence', 'key_confidence', 'mode_confidence']
    df = pd.read_csv('../data/spotify_final.csv').drop('Unnamed: 0', axis=1)

    def __init__(self, song_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.song_name = song_name
        self.song_id = None
        self.track_data = []

    def find_song(self):
        spotify = SpotifyAPI()
        song_id = 0
        song_name = self.song_name
        i = 0
        song_search = spotify.search({"track": song_name}, search_type="track")
        if len(song_search['tracks']['items']) > 0:
            while i < len(song_search['tracks']['items']):
                if self.song_name == song_search['tracks']['items'][i]['name']:
                    song_id = song_search['tracks']['items'][i]['id']
                    return song_id
                else:
                    i += 1
            if song_id != 0:
                return song_id
            else:
                return 404
        else:
            return 404
        return 404

    def get_track_data(self):
        song_id = self.song_id
        spotify = SpotifyAPI()
        track = spotify.get_track(song_id)
        self.track_data.append(track['name'])
        self.track_data.append(track['album']['name'])
        self.track_data.append(track['artists'][0]['name'])
        self.track_data.append(track['popularity'])
        self.track_data.append(track['id'])
        self.track_data.append(int(track['explicit']))

    def get_track_features(self):
        song_id = self.song_id
        spotify = SpotifyAPI()
        track_features = spotify.get_features(song_id)
        self.track_data.append(track_features['danceability'])
        self.track_data.append(track_features['energy'])
        self.track_data.append(track_features['key'])
        self.track_data.append(track_features['loudness'])
        self.track_data.append(track_features['mode'])
        self.track_data.append(track_features['speechiness'])
        self.track_data.append(track_features['acousticness'])
        self.track_data.append(track_features['instrumentalness'])
        self.track_data.append(track_features['liveness'])
        self.track_data.append(track_features['valence'])
        self.track_data.append(track_features['tempo'])
        self.track_data.append(track_features['duration_ms'])
        self.track_data.append(track_features['time_signature'])

    def get_track_analysis(self):
        song_id = self.song_id
        spotify = SpotifyAPI()
        track_analysis = spotify.get_analysis(song_id)
        self.track_data.append(track_analysis['track']['num_samples'])
        self.track_data.append(track_analysis['track']['duration'])
        self.track_data.append(track_analysis['track']['end_of_fade_in'])
        self.track_data.append(track_analysis['track']['start_of_fade_out'])
        self.track_data.append(track_analysis['track']['tempo_confidence'])
        self.track_data.append(track_analysis['track']['time_signature_confidence'])
        self.track_data.append(track_analysis['track']['key_confidence'])
        self.track_data.append(track_analysis['track']['mode_confidence'])

    def search(self):
        self.song_id = self.find_song()
        if self.song_id == 404:
            raise Exception("Song not found.")
        else:
            self.get_track_data()
            self.get_track_features()
            self.get_track_analysis()
        return pd.DataFrame([self.track_data], columns=self.col_name)

    def print_recommendations(self, indi, rec_df):
        print(f"For the song {self.song_name} by {rec_df['artist'].iloc[indi[0]]}, we recommend you check out:\n")
        artist_already_featured = []
        c = 0
        for i in indi[1:]:
            if rec_df['artist'].iloc[i] in artist_already_featured:
                pass
            else:
                print(f"{c+1}. {rec_df['song'].iloc[i].title()} by {rec_df['artist'].iloc[i].title()}\n")
                artist_already_featured.append(rec_df['artist'].iloc[i])
                c += 1
                if c >= 10:
                    break


    def recommend(self):
        search_df = self.search()
        rec_df = pd.concat([self.df, search_df], ignore_index=True)
        features = [x for x in self.df.columns if x not in ['song', 'album', 'artist', 'track_id', 'year', 'decade', 'genres']]
        cosine_similarities = cosine_similarity(rec_df[features])
        indicies = pd.Series(rec_df.index, index=rec_df['song'])
        idx = indicies[self.song_name]
        sim_scores = list(enumerate(cosine_similarities[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        indi = [i[0] for i in sim_scores]
        return self.print_recommendations(indi, rec_df)
