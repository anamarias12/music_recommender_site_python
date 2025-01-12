import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Initialize Spotify client
client_credentials = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=client_credentials)

def get_song_album_cover_url(song, artist):
    search_query = f"{song} {artist}"
    try:
        results = sp.search(q=search_query, type="track")
        if results['tracks']['items']:
            album_cover_url = results['tracks']['items'][0]['album']['images'][0]['url']
            return album_cover_url
        else:
            return "https://i.postimg.cc/0QNxYz4V/social.png"
    except Exception as e:
        st.error(f"An error occurred while fetching the album cover: {e}")
        return "https://upload.wikimedia.org/wikipedia/commons/3/37/Sad-face.png"

def recommend(index):
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music = []
    recommended_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        song = music.iloc[i[0]].song
        print(artist)
        print(song)
        recommended_music_posters.append(get_song_album_cover_url(song, artist))
        recommended_music.append(f"{song} - {artist}")

    return recommended_music, recommended_music_posters

st.header('Music Recommender System')

# Load data with error handling
try:
    music = pickle.load(open('data', 'rb'))
    similarity = pickle.load(open('similarity', 'rb'))
except FileNotFoundError:
    st.error("Data file not found. Please ensure 'data' and 'similarity' are in the correct directory.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading data: {e}")
    st.stop()

# Create a list of formatted strings with song name and artist name
music_list = [f"{row['song']} - {row['artist']}" for index, row in music.iterrows()]

selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    # Extract the song name from the selected option
    selected_song_name = selected_song.split(' - ')[0]
    index = music[music['song'] == selected_song_name].index[0]
    recommended_music, recommended_music_posters = recommend(index)
    for name, poster in zip(recommended_music, recommended_music_posters):
        st.write(name)
        st.image(poster)