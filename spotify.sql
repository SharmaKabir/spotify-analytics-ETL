create database spotify_db;
use spotify_db;

CREATE TABLE IF NOT EXISTS spotify_tracks(
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT,
    UNIQUE KEY unique_track (track_name, artist)
)

SHOW TABLES;

SELECT * FROM spotify_tracks;

SELECT track_name, artist, album, popularity
FROM spotify_tracks
ORDER BY popularity DESC
LIMIT 1;

SELECT AVG(popularity) AS average_popularity
FROM spotify_tracks;

SELECT track_name, artist, duration_minutes
FROM spotify_tracks
WHERE duration_minutes > 4.0;

SELECT 
    CASE 
        WHEN popularity >= 80 THEN 'Very Popular'
        WHEN popularity >= 50 THEN 'Popular'
        ELSE 'Less Popular'
    END AS popularity_range,
    COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY popularity_range;

 --DROP TABLE IF EXISTS spotify_tracks;

 SELECT * FROM spotify_tracks
 WHERE track_name LIKE '%love%'

 -- Check for exact duplicate track_name/artist combinations
SELECT track_name, artist, COUNT(*) as count
FROM spotify_tracks
GROUP BY track_name, artist
HAVING COUNT(*) > 1;