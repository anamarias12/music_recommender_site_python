# music_recommender_site_python

Foloseste cosine similarity
tag -> vector -> vectorization -> distance -> see similarity

Ai grija sa ai toate librariile descaracte, o chestie ar fi pt tokenizer sa ai chestia asta import nltk, nltk.download('punkt').

Trebuie facut cont pe Spotify for Developers dc vrei sa ai functionalitati nice de acolo precum poze de pe albume sau daca putem abilitatea de a da play la cantece. Trebuie sa apesi pe buton ca faci aplicatie sa ii dai un nume bla bla si sa intrii la settings unde ai CLIENTID si CLIENTSECRET.

https://spotipy.readthedocs.io/en/2.16.0/#client-credentials-flow

In terminal ruleaza: streamlit run app.py

Poti folosi si comanda jupyter notebook pt a schimba chestii in model_training si sa intrii pe linkul lor cu localhost

Asta e un model de pe documentatia spotify:
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()