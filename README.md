# music_recommender_site_python

Proiectul a fost realizat in Flask, majoritar in python cu parti de html, css si javascript. El reprezinta o pagina web unde pot
fi selectate cantece pe baza carora sunt oferite recomandari de muzica.

Recomandarile sunt facute pe baza cosine similarity. Tot ceea ce inseamna calcul al similitudinii a fost realizat in jupyter notebook.

Trebuie facut cont pe Spotify for Developers de unde vor fi luate CLIENTID si CLIENTSECRET. Acestea trebuie setate ca variabile de environment.

https://spotipy.readthedocs.io/en/2.16.0/#client-credentials-flow

Asta e un model de pe documentatia spotify:
from spotipy.oauth2 import SpotifyClientCredentials

Fisierele sunt prea mari asa ca pt a face git push:
git lfs track "similarity" "spotify_millsongdata.csv"

Pentru a folosi website-ul doar cautati un cantec anume in searchbar, selectati-l in lista si vor aparea recomandari bazate pe similitudinea cu
ce s-a ales. Apasarea pe coverul recomandarilor duce la redirectarea spre pagina acestora de spotify.

RULARE: python3 app.py

