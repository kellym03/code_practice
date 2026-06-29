# Real World Migration Tools

In real-world projects, we don't run raw SQL migrations. We use tools that help:

    Track which migrations have been applied.
    Organize migrations in files.
    Apply and roll back safely.

## Popular Tools
Tool 	        Language 	Notes
Goose 	        Go 	        Native Go tool
Flyway 	        Java, etc. 	Simple file-based
Liquibase 	    Java 	    More config-heavy
Alembic 	    Python 	    For SQLAlchemy
Prisma Migrate 	TypeScript 	Works with Prisma ORM
Drizzle Kit 	TypeScript 	Works with Drizzle ORM

## Real world migration
Use the terms up migration and down migration - up being to add and down being to roll back


## Example Workflow With a Tool
This will vary according to the tool you use.

    Write migration files.
        001_add_columns_to_transactions.up.sql
        001_add_columns_to_transactions.down.sql
    Apply them using a CLI:

    migrate up

# SQLite Data Types
NULL – Null value.
INTEGER – Signed integer stored in 0, 1, 2, 3, 4, 6, or 8 bytes.
REAL – Floating-point value stored as a 64-bit IEEE floating-point number.
TEXT – Text string stored using the database encoding, most commonly UTF-8.
BLOB – Short for Binary Large Object and typically used for images, audio, or other multimedia.
BOOLEAN – Boolean values are written in SQLite queries as true or false, but are recorded as 1 or 0.

# Constraints
CREATE TABLE employees(
  id INTEGER PRIMARY KEY, --saying this column is the primary key
  -- The PRIMARY KEY constraint uniquely identifies each row in the table
  name TEXT UNIQUE, -- this column requires unique values
  -- The UNIQUE constraint ensures that no two rows can have the same value in the 'name' column
  title TEXT NOT NULL -- this column will not allow null values
  -- The NOT NULL constraint ensures that the 'title' column cannot have NULL values
);

SQLite doesn't allow you to ADD CONSTRAINT in an ALTER TABLE statement but other versions of SQL do. 

## Primary Keys
The primary key is usually an ID

## Foreign Keys
This is what makes relational databases relational

### Creating a Foreign Key in SQLite

Creating a FOREIGN KEY in SQLite happens at table creation! After we define the table fields and constraints we add a named CONSTRAINT where we define the FOREIGN KEY column and its REFERENCES.

Here's an example:
CREATE TABLE departments (
  id INTEGER PRIMARY KEY,
  department_name TEXT NOT NULL
);

CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  department_id INTEGER,
  CONSTRAINT fk_departments
    FOREIGN KEY (department_id)
    REFERENCES departments(id)
);

# SQL Functions
IIF works like a ternary function and creates an additional column at the end of a table based on the arguments.
SELECT *,
  IIF (was_successful = TRUE, 'No action required', 'Perform an audit') AS audit
FROM transactions;

## BETWEEN
SELECT product_name, quantity
FROM products
WHERE quantity NOT BETWEEN 20 AND 100;

## DISTINCT
SELECT DISTINCT country_code
FROM users;

## IN
Another variation to the WHERE clause we can utilize is the IN operator. IN returns true or false if the first operand matches any of the values in the second operand. The IN operator is a shorthand for multiple OR conditions.

SELECT product_name, shipment_status
FROM products
WHERE shipment_status IN ('shipped', 'preparing', 'out of stock');

SELECT product_name, shipment_status
FROM products
WHERE shipment_status = 'shipped'
  OR shipment_status = 'preparing'
  OR shipment_status = 'out of stock';

# Like
Sometimes we don't have the luxury of knowing exactly what it is we need to query. Have you ever wanted to look up a song or a video but you only remember part of the name? SQL offers us an option for when we're in situations LIKE this.

The LIKE keyword allows for the use of the % and _ wildcard operators. Let's focus on % first.

## % Operator
The % operator will match zero or more characters. We can use this operator within our query string to find more than just exact matches, depending on where we place it.

SELECT * FROM products
WHERE product_name LIKE 'banana%';

SELECT * FROM products
WHERE product_name LIKE '%banana%';

##Underscore Operator
As discussed, the % wildcard operator matches zero or more characters. The _ wildcard operator, on the other hand, matches only a single character.

SELECT * FROM products
WHERE product_name LIKE '__oot';

# Practice
SELECT *,
  IIF ((age > 55 OR country_code = "CA"), 10, 0) AS discount_percent
FROM users;

# ORDER BY & LIMIT
ORDER BY must come before LIMIT

SELECT * FROM transactions
WHERE amount BETWEEN 10 AND 80
ORDER BY amount DESC
LIMIT 4;

# Aggregations
These are the functions that compact the results of a sql query into an aggregate figure

List
COUNT()
SUM()
MAX() -- select the max value in the field
MIN()

GROUP BY 

SELECT user_id, SUM(amount) AS "balance"
FROM transactions
WHERE was_successful = TRUE
GROUP BY user_id;