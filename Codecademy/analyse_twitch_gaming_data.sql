SELECT *
FROM stream
LIMIT 20;

SELECT *
FROM chat
LIMIT 20;

-- Count unique games
SELECT DISTINCT (game)
FROM stream;

-- Count unique channels
SELECT DISTINCT (channel)
FROM stream;

-- Count unique devices per game
SELECT game, COUNT(DISTINCT device_id)
FROM stream
GROUP BY game
ORDER BY 2 DESC;

-- Count number of streams per country for 'League of Legends'
SELECT game, country, COUNT(*)
FROM stream
WHERE game = 'League of Legends'
GROUP BY country
ORDER BY 3 DESC;

-- Classify games into genres
SELECT
  game,
  CASE
    WHEN game = 'League of Legends' THEN 'MOBA'
    WHEN game = 'Dota 2' THEN 'MOBA'
    WHEN game = 'Heroes of the Storm' THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive' THEN 'FPS'
    WHEN game = 'DayZ' THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved' THEN 'Survival'
    ELSE 'Other'
  END AS genre
FROM stream
GROUP BY 1
ORDER BY 2;

-- List first 10 timestamps
SELECT time
FROM stream
LIMIT 10;

-- Extract hour from time
SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;

-- Count unique devices streaming in each hour in Australia
SELECT
   strftime('%H', time),
   COUNT(DISTINCT device_ID),
   country
FROM stream
WHERE country = 'AU'
GROUP BY 1;

-- Join stream and chat tables
SELECT *
FROM stream
JOIN chat ON stream.device_id = chat.device_id
LIMIT 20;