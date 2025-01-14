from flask import Flask, render_template, request
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Initialize Spotify client
client_credentials = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=client_credentials)

# Flask app setup
app = Flask(__name__)

# Load data
try:
    music = pickle.load(open('data', 'rb'))
    similarity = pickle.load(open('similarity', 'rb'))
except FileNotFoundError:
    raise Exception("Data file not found. Ensure 'data' and 'similarity' files exist.")

# Function to get album cover URL
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
        return "https://upload.wikimedia.org/wikipedia/commons/3/37/Sad-face.png"

# Function to get song URL
def get_spotify_url(song_title, artist_name=None):
    query = f"{song_title} {artist_name}" if artist_name else song_title
    try:
        results = sp.search(q=query, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return track['external_urls']['spotify']
        else:
            return None
    except Exception as e:
        return None

# Recommendation function
def recommend(index):
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music = []
    recommended_music_posters = []
    recommended_links = []

    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        song = music.iloc[i[0]].song
        recommended_music_posters.append(get_song_album_cover_url(song, artist))
        recommended_music.append(f"{song} - {artist}")
        recommended_links.append(get_spotify_url(song, artist))

    return recommended_music, recommended_music_posters, recommended_links

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        selected_song = request.form.get('song')
        selected_song_name = selected_song.split(" - ")[0]
        index = music[music["song"] == selected_song_name].index[0]
        recommended_music, recommended_music_posters, recommended_links = recommend(index)
        return render_template(
            'recommendations.html',
            songs=zip(recommended_music, recommended_music_posters, recommended_links)
        )

    music_list = [f"{row['song']} - {row['artist']}" for index, row in music.iterrows()]
    return render_template('search.html', music_list=music_list)


if __name__ == '__main__':
    app.run(debug=True)
