--1. List each question in the survey along with the number of unique users who responded to that question.
 SELECT question_text, COUNT(DISTINCT(user_id)) AS 'Users who responded'
 FROM survey_responses
 GROUP BY question_text

-- Compare funnels for AB Tests
-- List each onboarding modal along with the number of unique users who saw that modal.
select modal_text, COUNT(DISTINCT user_id)
from onboarding_modals
GROUP BY modal_text
ORDER BY modal_text

-- List each onboarding modal along with the number of unique users who clicked on that modal, broken out by AB test group.
SELECT modal_text, 
  COUNT(DISTINCT CASE 
    WHEN ab_group = 'control' THEN user_id
    END) as 'control clicks',
  COUNT(DISTINCT CASE 
    WHEN ab_group = 'variant' THEN user_id
    END) as 'variant clicks'
FROM onboarding_modals
GROUP BY modal_text
ORDER BY modal_text

-- Build a funnel from multiple tables
-- List the first 50 users who browsed, checked out, and purchased, along with the timestamps of each action.
SELECT *
FROM 
  browse AS b
LEFT JOIN 
  checkout AS c ON b.user_id = c.user_id 
LEFT JOIN 
  purchase AS p ON b.user_id = p.user_id 
LIMIT 50

-- List the first 50 users who browsed, checked out, and purchased, along with boolean indicators of whether they completed each step.
SELECT DISTINCT 
  b.browse_date,
  b.user_id,
  c.user_id IS NOT NULL AS 'is_checkout',
  p.user_id IS NOT NULL AS 'is_purchase'
FROM 
  browse AS b
LEFT JOIN 
  checkout AS c ON b.user_id = c.user_id 
LEFT JOIN 
  purchase AS p ON b.user_id = p.user_id 
LIMIT 50

-- Calculate the conversion rates between each step of the funnel.
WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id AS 'is_browse',
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)

SELECT 
  COUNT(is_browse) AS num_browse,
  SUM(is_checkout) AS 'num_checkout',
  SUM(is_purchase) AS 'num_checkout',
  ROUND(1.0 * SUM(is_checkout) / COUNT(is_browse), 2) AS 'Checkout CVR',
  ROUND(1.0 * SUM(is_purchase) / SUM(is_checkout), 2) AS 'Purchase CVR'
FROM funnels

-- Calculate the conversion rates between each step of the funnel, broken out by day.
WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id,
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)
SELECT 
   browse_date,
   COUNT(*) AS 'num_browse',
   SUM(is_checkout) AS 'num_checkout',
   SUM(is_purchase) AS 'num_purchase',
   1.0 * SUM(is_checkout) / COUNT(user_id) AS 'browse_to_checkout',
   1.0 * SUM(is_purchase) / SUM(is_checkout) AS 'checkout_to_purchase'
FROM funnels
GROUP BY browse_date