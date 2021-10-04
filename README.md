# Billboard Hot 100 Music Recommender
## Executive Summary

**Problem Statement:** As growth in the accessibility of technology with high computation power, along with the availability of free education, has skyrocketed, music creation is easier to get into then ever before. This has led to a boom in the number of artists putting out music on various platforms such as Apple Music, Spotify, and Soundcloud, which only compounds year after year. As more and more new artists are added year after year, older artists tend to be left in the past. Most music discovery platforms focus on current trends so they will rarely recommend anything that wouldn't' be considered somewhat recent. I want to solve this problem, by creating a recommendation model that can be used to suggest songs that made it to the Billboard Hot 100 in the years 1960-1999 given a user input song.


**Project Flow:** There will be 6 sections to this project each explained below. However, if you are only interested in the recommendations skip directly to 06-GET-RECOMMENDATIONS.
1. 01-web-scrape-billboard-hot-100
2. 02-spotify-auth
3. 03-hot100-feature-and-analysis
4. 04-EDA
5. 05-recommender-model
6. 06-GET-RECOMMENDATIONS

**Data:** The Billboard Hot 100 data was gathered via web scraping the pages from [Wikipedia]('https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_1960') for the year 1960-1999. All metadata for the Hot 100 songs was gathered via the [Spotify WebAPI]("https://developer.spotify.com/documentation/web-api/").

**Recommender Model:** This project will use a content based recommendation model. I have collected metadata from the Spotify WebAPI for each song item listed in the hot100 dataset. Recommendations will be generated and ranked via the cosine similarity score. Cosine similarity score was chosen due to it being lighter on computational power and works irrespective of the variable sizes. 


**Data Dictionary**

|Variable   |Description   |Dataset   |
|---|---|---|
|Song  | Name of Song  | hot100_60-99  |
|Artist(s) | Name of Artist  | hot100_60-99  |
|year | Year song appeared on Hot 100  | hot100_60-99  |
|song| Name of song| spotify_final|
|album| Name of album | spotify_final|
|artist| Name of artist| spotify_final|
|popularity| Popularity of song| spotify_final|
|track_id| Spotify Track ID|spotify_final|
|track_explicit| Song Explicit True/False|spotify_final|
|danceability| Feature Statistic|spotify_final|
|energy| Feature Statistic|spotify_final|
|key| Feature Statistic|spotify_final|
|loudness| Feature Statistic|spotify_final|
|mode| Feature Statistic|spotify_final|
|speechiness| Feature Statistic|spotify_final|
|acousticness| Feature Statistic|spotify_final|
|instrumentalness| Feature Statistic|spotify_final|
|liveness| Feature Statistic|spotify_final|
|valence| Feature Statistic|spotify_final|
|tempo| Feature Statistic|spotify_final|
|duration| Feature Statistic|spotify_final|
|time_signiture| Feature Statistic|spotify_final|
|num_samples| Feature Analysis|spotify_final|
|duration| Feature Analysis|spotify_final|
|end_of_fade_in| Feature Analysis|spotify_final|
|start_of_fade_out| Feature Analysis|spotify_final|
|tempo_confidence| Feature Analysis|spotify_final|
|time_signiture_confidence| Feature Analysis|spotify_final|
|key_confidence| Feature Analysis|spotify_final|
|mode_confidence| Feature Analysis|spotify_final|
|genres| Artist Genre from Spotify | spotify_final|
|year| Year on Hot 100| spotify_final|
|decade| Decade in Hot 100| spotify_final|

**
