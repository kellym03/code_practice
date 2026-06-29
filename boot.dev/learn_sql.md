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
