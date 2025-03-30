import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

load_dotenv()

db_config={
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'spotify_db'
}

def update_schema():
    """Add release_date column to spotify_tracks table"""
    connection= mysql.connector.connect(**db_config)
    cursor=connection.cursor()
    cursor.execute("SHOW COLUMNS FROM spotify_tracks LIKE 'release_date'")
    column_exists=cursor.fetchone()
    if not column_exists:
        cursor.execute("ALTER TABLE spotify_tracks ADD COLUMN release_date DATE")
        print("column add done")
    cursor.close()
    connection.close()


def fetch_release_dates():
    """Fetch release dates for tracks and update the database"""
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
    ))
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT id, track_name, artist FROM spotify_tracks WHERE release_date IS NULL")
    tracks = cursor.fetchall()
    updated_count = 0
    for track_id, track_name, artist in tracks:
        try:
            search_query = f"track:{track_name} artist:{artist}"
            results = sp.search(search_query, type='track', limit=1)
            if results['tracks']['items']:
                track = results['tracks']['items'][0]
                album = track['album']
                release_date = album['release_date']
                #normalise
                if len(release_date) == 4: 
                    release_date = f"{release_date}-01-01"
                elif len(release_date) == 7:
                    release_date = f"{release_date}-01"
                cursor.execute(
                    "UPDATE spotify_tracks SET release_date = %s WHERE id = %s",
                    (release_date, track_id)
                )
                connection.commit()
                updated_count += 1
                if updated_count % 20 == 0:
                    print(f"Updated {updated_count} tracks with release dates DONE")
                
        except Exception as e:
            print(f"Error updating {track_name}: {e}")
    
    print(f" {updated_count} tracks with release dates DONE")
    cursor.close()
    connection.close()   