# Relational vs Non-relation databases

The big difference between relational and non-relational databases is that non-relational databases tend to nest their data. Instead of always keeping records in separate tables, they often store records within other records.

To over-simplify it, you can think of non-relational databases as giant JSON blobs. If a user can have multiple courses, you might just add all the courses to the user record.

{
"users": [
{
"id": 0,
"name": "Elon",
"courses": [
{
"name": "Biology",
"id": 0
}
]
},
{
"id": 1,
"name": "Curly",
"courses": [
{
"name": "Biology",
"id": 0
}
]
}
]
}

# CRUD

create - HTTP POST
read - HTTP GET
update - HTTP PUT
delete - HTTP DELETE

# HTTP CRUD Database lifecycle

1. The frontend processes some data from user input – maybe a form is submitted.
2. The frontend sends that data to the server through an HTTP request – maybe a POST.
3. The server makes a SQL query to its database to create an associated record – probably using an INSERT statement.
4. Once the server has determined that the DB query was successful, it responds to the frontend with a status code. Hopefully a 200-level code (success)!

# Insert statement

INSERT INTO users(id, name, age, country_code, username, password, is_admin)
VALUES (1, 'David', 34, 'US', 'DavidDev', 'insertPractice', FALSE);

# Auto Increment

Many dialects of SQL support an AUTO INCREMENT feature. When inserting records into a table with AUTO INCREMENT enabled, the database will assign the next value automatically. In SQLite, an integer id field that has the PRIMARY KEY constraint will auto-increment by default!

## IDs

Depending on how your database is set up, you may be using traditional ids or you may be using UUIDs. SQL doesn't support auto-incrementing a uuid, so if your database is using them your server will have to handle the changing uuids for each record.

# Manual Entry

In the real world a server will use a language like Go or Python to interface with a database and it will use something string interpolation to send communications like the below (GO language):

sqlQuery := fmt.Sprintf(`INSERT INTO users(name, age, country_code)
VALUES ('%s', %v, '%s');`, user.Name, user.Age, user.CountryCode)

# HTTP CRUD Database Lifecycle

First, the front-end webpage loads.
The front-end sends an HTTP GET request to a /users endpoint on the back-end server.
The server receives the request.
The server uses a SELECT statement to retrieve the user's record from the users table in the database.
The server converts the row of SQL data into a JSON object and sends it back to the front-end.

# WHERE Clause

can use IS NOT NULL and IS NULL

# DELETE Statement

DELETE FROM employees
WHERE id = 251;

# Caution deleting data

Deleting data can be risky and you need to have ways to restore it just in case:
If you're using a cloud-service like GCP's Cloud SQL or AWS's RDS you should always turn on automated backups. They take an automatic snapshot of your entire database on some interval, and keep it around for some length of time.
A "soft delete" is when you don't actually delete data from your database, but instead just "mark" the data as deleted. For example, you might set a deleted_at date on the row you want to delete. Then, in your queries you ignore anything that has a deleted_at date set. The idea is that this allows your application to behave as if it's deleting data, but you can always go back and restore any data that's been removed.

# UPDATE Query in SQL

UPDATE employees
SET job_title = 'Backend Engineer', salary = 150000
WHERE id = 251;

# Object Relational Mapping (ORMs)

An Object-Relational Mapping or an ORM for short, is a tool that allows you to perform CRUD operations on a database using a traditional programming language. These typically come in the form of a library or framework that you would use in your backend code. The primary benefit an ORM provides is that it maps your database records to in-memory objects.

ORM example in GO
user := User{
ID: 10,
Name: "Lane",
IsAdmin: false,
}

// generates a SQL statement and runs it,
// creating a new record in the users table
db.Create(user)

Example using straight SQL
user := User{
ID: 10,
Name: "Lane",
IsAdmin: false,
}

db.Exec("INSERT INTO users (id, name, is_admin) VALUES (?, ?, ?);",
user.ID, user.Name, user.IsAdmin)

This will always be a team decision, deciding whether or not to use an ORM. It is trading control for simplicity.

# Aggregations

## HAVING

remember that having typically comes in the running order before select so it won't know the aliasing until select is run even though you type having after having types select.

SELECT sender_id, SUM(amount) AS "balance"
FROM transactions
WHERE was_successful = TRUE
AND sender_id IS NOT NULL
AND note LIKE "%lunch%"
GROUP BY sender_id
HAVING SUM(amount) > 20
ORDER BY balance ASC;

## HAVING VS WHERE

A WHERE condition is applied to all the data in a query before it's grouped by a GROUP BY clause.
A HAVING condition is applied only to the grouped rows that are returned after a GROUP BY is applied.

## ROUND

ROUND(field, precision)

# Subqueries

Example

SELECT id, song_name, artist_id
FROM songs
WHERE artist_id IN (
SELECT id
FROM artists
WHERE artist_name LIKE 'Rick%'
);

In this hypothetical database, the query above selects all of the ids, song_names, and artist_ids from the songs table that are written by artists whose name starts with Rick. Notice that the subquery allows us to use information from a different table – in this case the artists table.

## Subquery Syntax

The only syntax unique to a subquery is the parentheses surrounding the nested query. The IN operator could be different; for example, we could use the = operator if we expect a single value to be returned.

You can't access the additional columns of data in table created by the subquery. You would need an actual join for this. Whereas this is like a 'soft join'. SQL will expect that the data perfectly aligns between the a like id from a users table and a user_id column in a transactions table.

SELECT \*
FROM transactions
WHERE user_id = (
SELECT id
FROM users
WHERE name = "David"
);

## SQLite vs other SQL

In SQLite the LIKE operator isn't case sensitive where in PostgreSQL it is case sensitive.
Additionally, in some systems when searching for columns you use the double quotes, "", but when searching for literals you should use single quotes, ''.

SELECT \*
FROM users
WHERE id IN (
SELECT sender_id
FROM transactions
WHERE note LIKE '%invoice%'
OR note LIKE '%tax%'
)
AND is_admin = FALSE;

## No Tables

A scalar subquery (a subquery that calculates and returns a single, independent mathematical value).

You can use a subquery to create values like in a full programming language to query against a main table.
SELECT _
FROM users
WHERE age_in_days > (
SELECT 365 _ 40
);

In the above example a person's age is stored in days rather than years and the years are assumed to have 365 days. This type of programming can be observed in production databases.

# Normalisation

# Table relationships

## Types of Relationships

There are 3 primary types of relationships in a relational database:
One-to-one
One-to-many
Many-to-many

## One to many

Creating a foreign relationship
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER NOT NULL,
country_code TEXT NOT NULL,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
is_admin BOOLEAN
);

CREATE TABLE devices (
id INTEGER PRIMARY KEY,
mac_address TEXT,
type TEXT,
user_id INTEGER,
CONSTRAINT fk_users
FOREIGN KEY (user_id)
REFERENCES users(id)
);

## Many to many

### Unique constraint across two fields

The UNIQUE constaint lets multiple rows share the same product_id or supplier_id, but it prevents any two rows from having both the same product_id and supplier_id. For example, no combination of supplier and product IDs should allow there to be an instance where a two rows contain the same combination of product and supplier IDs.

CREATE TABLE product_suppliers (
product_id INTEGER,
supplier_id INTEGER,
UNIQUE(product_id, supplier_id),
FOREIGN KEY (product_id) REFERENCES products (id),
FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
);

Assignment but good principles to consider in chains of logic"
Let's rethink our user ↔ country relationship. Originally, each user had a single country_code field, but many users have dual citizenship!

If we just gave the countries table a user_id (a one-to-many relationship), we would have duplicate country records. If two users are associated with the United States, we'd create two "United States" countries records.

It is better if each country only has a single record. That way, when a country changes its metadata, we only have to update one record. Because a user can have many countries, and a country can have many users, this is a many-to-many relationship.

## Database normalisation

### What Is Data Integrity?

"Data integrity" refers to the accuracy and consistency of data. For example, if a user's age is stored in a database, rather than their birthday, that data becomes incorrect automatically with the passage of time.
It would be better to store a birthday and calculate the age as needed.

### What Is Data Redundancy?

"Data redundancy" occurs when the same piece of data is stored in multiple places. For example: saving the same file multiple times to different hard drives.
Data redundancy can be problematic, especially when data in one place is changed such that the data is no longer consistent across all copies of that data.

## Normal Forms

You can imagine the below like an onion starting with the outer layer and going in:
First normal form (1NF) - least normalised
Second normal form (2NF)
Third normal form (3NF)
Boyce-Codd normal form (BCNF) - most normalised

The more normalised a database the better its integrity and less duplicate data there is.

### Primary key in normal forms

When we're talking more generally about data normalization, the term "primary key" means the collection of columns that uniquely identify a row. That can be a single column, but it can actually be any number of columns that form a composite key. A primary key is the minimum number of columns needed to uniquely identify a row in a table.

If you think back to the many-to-many joining table product_suppliers, that table's "primary key" was actually a combination of the two IDs, product_id and supplier_id:
CREATE TABLE product_suppliers (
product_id INTEGER,
supplier_id INTEGER,
UNIQUE(product_id, supplier_id)
);

## First Normal Form

It must have a unique primary key.
A cell can't have a nested table as its value (depending on the database system you're using, this may not even be possible).

## Second Normal Form

All columns that are not part of the primary key are dependent on the entire primary key, and not just one of the columns in the primary key.

first_name last_name first_initial
Lane Wagner l
Lane Small l
Allan Wagner a
This table does not adhere to 2NF. The first_initial column is entirely dependent on the first_name column, rendering it redundant. first_initial doesn't depend on last_name at all.

You should probably default to keeping your tables in second normal form. That said, there are good reasons to deviate from it, particularly for performance reasons. The reason being that when you have to query a second table to get additional data, it can take a bit longer.

My (Lane Wagner's) rule of thumb is: optimize for data integrity and data de-duplication first. If you have speed issues, de-normalize accordingly.

## Third Normal Form

A table in third normal form (3NF) follows all the rules of second normal form, and one additional rule:

All columns that aren't part of the primary key are dependent solely on the primary key.

### Example of 2NF but Not 3NF

In this table, the primary key is simply the id column.

id name first_initial email
1 Lane l lane.works@example.com
2 Breanna b breanna@example.com
3 Lane l lane.right@example.com
This table is in second normal form because first_initial is not dependent on a part of the primary key. However, because it is dependent on the name column, it doesn't adhere to third normal form.

### Example of 3NF

The way to convert the table above to 3NF is to add a new table that maps a name directly to its first_initial. Notice how similar this solution is to 2NF.

id name email
1 Lane lane.works@example.com
2 Breanna breanna@example.com
3 Lane lane.right@example.com

name first_initial
Lane l
Breanna b

## Boyce-Codd Normal Form

A table in Boyce-Codd normal form (created by Raymond Boyce and Edgar Codd) follows all the rules of third normal form, plus one additional rule:

A column that's part of a primary key can not be entirely dependent on a column that's not part of that primary key.

This only comes into play when there are multiple possible primary key combinations that overlap. Another name for this is "overlapping candidate keys."

I feel really shakey about this. Definitely a weak area for me.

# Normalisation review

The exact definitions of 1st, 2nd, 3rd and Boyce-Codd normal forms simply are not all that important in your work as a back-end developer.

## Rules of Thumb for Database Design

Every table should always have a unique identifier (primary key)
90% of the time, that unique identifier will be a single column named id
Avoid duplicate data
Avoid storing data that is completely dependent on other data. Instead, compute it on the fly when you need it.
Keep your schema as simple as you can. Optimize for a normalized database first. Only denormalize for speed's sake when you start to run into performance problems.
