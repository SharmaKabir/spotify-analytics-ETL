import re 
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mysql.connector

sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='83fdcabb5af747099c7fb41eef106eef',
    client_secret='acc26dd865824209877b1ab0d72ce587'
                                                         
))