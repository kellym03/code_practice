--1. Select all columns from the survey table
 SELECT *
 FROM survey
 LIMIT 10;

--2. Count the number of responses for each question in the survey
 SELECT 
   question,
   COUNT(response)
 FROM survey
 GROUP BY question
 ORDER BY 1

--3. Calculate the conversion rate from the first question ("What are you looking for?") for the rest of the questions in the survey
WITH QuestionCounts AS (
    -- 1. Get the count for each question
    SELECT
        question,
        COUNT(response) AS response_count
    FROM
        survey
    GROUP BY
        question
),
OrderedCounts AS (
    -- 2. Order the questions to easily identify the first one ('What are you looking for?')
    SELECT
        question,
        response_count,
        ROW_NUMBER() OVER (ORDER BY
            CASE
                WHEN question = 'What are you looking for?' THEN 1
                ELSE 2
            END, question
        ) AS rn -- Row number for ordering
    FROM
        QuestionCounts
)
-- 3. Calculate the Conversion Rate
SELECT
    oc.question,
    oc.response_count AS "COUNT(response)",
    -- Use a Window Function to find the count of the first question and divide
    CAST(oc.response_count AS REAL) / MAX(CASE WHEN oc.rn = 1 THEN oc.response_count ELSE NULL END) OVER () AS conversion_rate
FROM
    OrderedCounts oc
ORDER BY
    oc.rn;

--4. For each user who took the quiz, indicate whether they used the home try-on program and whether they made a purchase
SELECT
  q.user_id,
  CASE
    WHEN h.user_id IS NOT NULL THEN 'TRUE'
    ELSE 'FALSE'
  END AS is_home_try_on,
  CAST(number_of_pairs AS INTEGER) AS number_of_pairs,
  CASE
    WHEN p.user_id IS NOT NULL THEN 'TRUE'
    ELSE 'FALSE'
  END AS is_purchase
FROM quiz AS q
LEFT JOIN home_try_on AS h ON q.user_id = h.user_id
LEFT JOIN purchase AS p ON q.user_id = p.user_id
GROUP BY q.user_id

--5. Calculate the purchase rate for users who used the home try-on program, broken out by the number of pairs they ordered
WITH t1 AS (SELECT
  q.user_id,
  CASE
    WHEN q.user_id IS NOT NULL THEN '1'
    ELSE '0'
  END AS is_browser,
  CASE
    WHEN h.user_id IS NOT NULL THEN '1'
    ELSE '0'
  END AS is_home_try_on,
  CAST(number_of_pairs AS INTEGER) AS number_of_pairs,
  CASE
    WHEN p.user_id IS NOT NULL THEN '1'
    ELSE '0'
  END AS is_purchase
FROM quiz AS q
LEFT JOIN home_try_on AS h ON q.user_id = h.user_id
LEFT JOIN purchase AS p ON q.user_id = p.user_id
GROUP BY q.user_id)

SELECT
  number_of_pairs,
  CAST(SUM(is_purchase) AS REAL) / SUM(is_home_try_on)
FROM t1
GROUP BY number_of_pairs