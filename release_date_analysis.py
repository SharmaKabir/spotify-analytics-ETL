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
