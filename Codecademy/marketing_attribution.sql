-- Identify the first touchpoint for each user
WITH first_touch AS (
   SELECT user_id,
      MIN(timestamp) AS 'first_touch_at'
   FROM page_visits
   GROUP BY user_id)
SELECT ft.user_id,
  ft.first_touch_at,
  pv.utm_source
FROM first_touch AS 'ft'
JOIN page_visits AS 'pv'
  ON ft.user_id = pv.user_id
  AND ft.first_touch_at = pv.timestamp;

-- Identify the last touchpoint for each user
WITH last_touch AS (
    SELECT user_id,
       MAX(timestamp) AS 'last_touch_at'
    FROM page_visits
    GROUP BY user_id)
SELECT lt.user_id,
   lt.last_touch_at,
   pv.utm_source
FROM last_touch AS 'lt'
JOIN page_visits AS 'pv'
   ON lt.user_id = pv.user_id
   AND lt.last_touch_at = pv.timestamp
WHERE lt.user_id = 10069;

-- Attribution queries project
SELECT 
  COUNT(DISTINCT utm_campaign)
FROM page_visits;

SELECT
  COUNT(DISTINCT utm_source),
FROM page_visits;

SELECT
  DISTINCT utm_source, utm_campaign
FROM page_visits;

SELECT
  DISTINCT page_name
FROM page_visits;

-- Count the number of users associated with each campaign by first touch
WITH first_touch AS (
   SELECT user_id,
      MIN(timestamp) AS 'first_touch_at'
   FROM page_visits
   GROUP BY user_id)
SELECT COUNT(ft.user_id),
  pv.utm_campaign
FROM first_touch AS 'ft'
JOIN page_visits AS 'pv'
  ON ft.user_id = pv.user_id
  AND ft.first_touch_at = pv.timestamp
GROUP BY utm_campaign;

-- Count the number of users associated with each campaign by last touch
WITH last_touch AS (
   SELECT user_id,
      MAX(timestamp) AS 'last_touch_at'
   FROM page_visits
   GROUP BY user_id)
SELECT COUNT(lt.user_id),
  pv.utm_campaign
FROM last_touch AS 'lt'
JOIN page_visits AS 'pv'
  ON lt.user_id = pv.user_id
  AND lt.last_touch_at = pv.timestamp
GROUP BY utm_campaign;

-- Count the number of users who made a purchase
SELECT 
  COUNT(DISTINCT user_id)
FROM page_visits
WHERE page_name = '4 - purchase';

-- Count the number of users who made a purchase by last touch campaign
WITH last_touch AS (
   SELECT user_id,
      MAX(timestamp) AS 'last_touch_at'
   FROM page_visits
   GROUP BY user_id)
SELECT COUNT(lt.user_id),
  pv.utm_campaign
FROM last_touch AS 'lt'
JOIN page_visits AS 'pv'
  ON lt.user_id = pv.user_id
  AND lt.last_touch_at = pv.timestamp
WHERE page_name = '4 - purchase'
GROUP BY utm_campaign;