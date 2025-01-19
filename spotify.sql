create database spotify_db;
use spotify_db;

CREATE TABLE IF NOT EXISTS spotify_tracks(
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
)
