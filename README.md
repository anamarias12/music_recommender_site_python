# music_recommender_site_python

Foloseste cosine similarity
tag -> vector -> vectorization -> distance -> see similarity

Ai grija sa ai toate librariile descaracte, o chestie ar fi pt tokenizer sa ai chestia asta import nltk, nltk.download('punkt').

Trebuie facut cont pe Spotify for Developers dc vrei sa ai functionalitati nice de acolo precum poze de pe albume sau daca putem abilitatea de a da play la cantece. Trebuie sa apesi pe buton ca faci aplicatie sa ii dai un nume bla bla si sa intrii la settings unde ai CLIENTID si CLIENTSECRET.

https://spotipy.readthedocs.io/en/2.16.0/#client-credentials-flow

Poti folosi si comanda jupyter notebook pt a schimba chestii in model_training si sa intrii pe linkul lor cu localhost

Asta e un model de pe documentatia spotify:
from spotipy.oauth2 import SpotifyClientCredentials

Fisierele sunt prea mari asa ca pt a face git push:
git lfs track "similarity" "spotify_millsongdata.csv"

RULARE: python3 app.py

TO DO:
- searchbar improvement
- filtering functionalities
- rating functionalities