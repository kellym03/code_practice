-- User churn analysis for a subscription-based service
-- churn rates typically don't include the additions made in a period only the losses divided by the starting value
 SELECT 
  100.0/2000.0;

SELECT
  (450.0) / 3000

-- subscriber churn rate
SELECT 1.0 * 
(
  SELECT COUNT(*)
  FROM subscriptions
  WHERE subscription_start < '2017-01-01'
  AND (
    subscription_end
    BETWEEN '2017-01-01'
    AND '2017-01-31'
  )
) / (
  SELECT COUNT(*) 
  FROM subscriptions 
  WHERE subscription_start < '2017-01-01'
  AND (
    (subscription_end >= '2017-01-01')
    OR (subscription_end IS NULL)
  )
) 
AS result;

-- subscriber churn rate using CTEs
WITH enrollments AS
(SELECT *
FROM subscriptions
WHERE subscription_start < '2017-01-01'
AND (
  (subscription_end >= '2017-01-01')
  OR (subscription_end IS NULL)
)),
status AS (
  SELECT
  CASE
    WHEN (subscription_end > '2017-01-31')
      OR (subscription_end IS NULL) THEN 0
    ELSE 1
  END as is_canceled,
  CASE
    WHEN (subscription_start < '2017-01-01')
      AND (
        (subscription_end >= '2017-01-01')
        OR (subscription_end IS NULL)
      ) THEN 1
    ELSE 0
  END as is_active
  FROM enrollments
)

SELECT 1.0 * SUM(is_canceled) / SUM(is_active)
FROM status;

-- generating a list of months using UNION
WITH months AS
(SELECT
  '2017-01-01' AS first_day,
  '2017-01-31' AS last_day
UNION
SELECT
  '2017-02-01' AS first_day,
  '2017-02-28' AS last_day
UNION
SELECT
  '2017-03-01' AS first_day,
  '2017-03-31' AS last_day
)

SELECT *
FROM months

-- cross join to get all combinations of subscriptions and months
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS(
SELECT *
FROM subscriptions
CROSS JOIN months 
LIMIT 100)

SELECT *
FROM cross_join

-- determining active subscriptions for each month
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),

status AS
(SELECT
  id,
  first_day AS month,
  CASE
    WHEN (subscription_start < first_day)
      AND (
        (subscription_end >= first_day)
        OR (subscription_end IS NULL)
      ) THEN 1
    ELSE 0
  END as is_active
FROM cross_join)

SELECT *
FROM status
LIMIT 100;

-- determining canceled subscriptions for each month
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
  CASE
    WHEN (subscription_end BETWEEN first_day AND last_day) THEN 1
    ELSE 0
  END as is_canceled
FROM cross_join)

SELECT *
FROM status
LIMIT 100;

-- determining both active and canceled subscriptions for each month
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
CASE 
  WHEN subscription_end BETWEEN first_day AND last_day THEN 1
  ELSE 0
END as is_canceled
FROM cross_join),
status_aggregate AS (
  SELECT
    month,
    SUM(is_active),
    SUM(is_canceled)
  FROM status
  GROUP BY month
)
SELECT *
FROM status_aggregate;

-- final churn rate calculation
WITH months AS (
  SELECT 
    '2017-01-01' AS first_day, 
    '2017-01-31' AS last_day 
  UNION 
  SELECT 
    '2017-02-01' AS first_day, 
    '2017-02-28' AS last_day 
  UNION 
  SELECT 
    '2017-03-01' AS first_day, 
    '2017-03-31' AS last_day
), 
cross_join AS (
  SELECT *
  FROM subscriptions
  CROSS JOIN months
), 
status AS (
  SELECT 
    id, 
    first_day AS month, 
    CASE
      WHEN (subscription_start < first_day) 
        AND (
          subscription_end > first_day 
          OR subscription_end IS NULL
        ) THEN 1
      ELSE 0
    END AS is_active, 
    CASE
      WHEN subscription_end BETWEEN first_day AND last_day THEN 1
      ELSE 0
    END AS is_canceled 
  FROM cross_join
), 
status_aggregate AS (
  SELECT 
    month, 
    SUM(is_active) AS active, 
    SUM(is_canceled) AS canceled 
  FROM status 
  GROUP BY month
) 
SELECT
  month, 
  1.0 * canceled / active AS churn_rate 
FROM status_aggregate;