-- codecademy.com practice - performing calculations with window function practice

-- Final project - Climate change analysis

-- 1 - Displays all the data from the state_climate table
SELECT *
FROM state_climate

-- 2 - Calculates the average temperature for each state over the years
SELECT 
  state,
  tempc,
  year,
  AVG(tempc) OVER (
    PARTITION BY state
    ORDER BY year
  ) 'average tempc'
FROM state_climate

-- 3 - Finds the lowest temperature recorded in each state
SELECT 
  state,
  year,
  tempc,
  FIRST_VALUE(tempc) OVER (
    PARTITION BY state
    ORDER BY tempc
  ) 'lowest_temp'
FROM state_climate

-- 4 - Finds the highest temperature recorded in each state
SELECT 
  state,
  year,
  tempc,
  FIRST_VALUE(tempc) OVER (
    PARTITION BY state
    ORDER BY tempc DESC
  ) 'highest_temp'
FROM state_climate

-- 5 - Calculates the change in temperature from the previous year for each state and finds the maximum change for each state
WITH t1 AS (
  SELECT 
    state,
    year,
    tempc,
    tempc - LAG(tempc, 1, tempc) OVER (
      PARTITION BY state
      ORDER BY year ASC
      ) 'temp_change'
  FROM state_climate as t1)

SELECT 
  state,
  MAX(temp_change)
  FROM t1
  GROUP BY state
  ORDER BY 2 DESC

-- 6 Calculates the coldest temperature of any state or year and ranks them
SELECT 
  state,
  year,
  tempc,
  RANK() OVER (
    ORDER BY tempc ASC
  ) AS 'coldest_rank'
FROM state_climate

-- 7 Calculates the hottest temperature of any state or year and ranks them AND finds the maximum rank for each state
WITH t1 AS (SELECT 
  state,
  year,
  tempc,
  RANK() OVER (
    ORDER BY tempc DESC
  ) AS 'warmest_rank'
FROM state_climate)

SELECT 
  state,
  year,
  tempc,
  MAX(warmest_rank)
FROM t1
GROUP BY state

-- 8 - Divides the temperature data for each state into quartiles
SELECT 
  state,
  year,
  NTILE(4) OVER (
  tempc,
    PARTITION BY state
    ORDER BY tempc 
  ) AS 'coldest_quartiles'
FROM state_climate

-- 9 - Divides the temperature data for all states into quintiles
SELECT 
  state,
  year,
  tempc,
  NTILE(5) OVER (
    ORDER BY tempc 
  ) AS 'coldest_quintiles'
FROM state_climate
