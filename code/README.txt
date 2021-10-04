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

**Data Dictionary**


**