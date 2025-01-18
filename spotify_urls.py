import re 
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv(SPOTIFY_CLIENT_ID),
    client_secret=os.getenv(SPOTIFY_CLIENT_SECRET)
                                                         
))