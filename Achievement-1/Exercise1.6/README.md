# Database in Python

## Create a MySQL database for Recipe App

## Relational Database Management Systems

(RDBMS) are systems to help you manage your database, including keeping it secure by controlling user access. MySQL is used as a RDBMS for the Recipe App

## After Installation

### Step 1

- Create New User:
  Open MySQL Command line => Enter Your root password
  ` CREATE USER 'cf-python'@'localhost' IDENTIFIED BY 'password';`
- To check if the user exists:
  `SELECT User, Host FROM mysql.user WHERE User='cf-python';`
- To Delete a user:
  `DROP USER 'user1'@'localhost', 'user2'@'localhost';`

### Step 2

- Grant Permission to User:
  mysql> `GRANT ALL PRIVILEGES ON * . * TO 'cf-python'@'localhost';`

### Step 3

- mysql> exist

## Installing and Importing the MySQL Connector for Python:

- First activate a virtual environment:

```bash
pip install mysql-connector-python
import mysql.connector
 conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')
```

- Initialize a new object
  `cursor = conn.cursor()`

#### Create Database

for SQL:
`CREATE DATABASE <database name>;`
for Python:

```bash
cursor.execute("<SQL query>")
cursor.execute("CREATE DATABASE my_database")
```

### use the database

MySQL: `USE <database name>`

iPython: `cursor.execute("USE my_database")`

### Create a table in MySQL

```bash
CREATE TABLE <table name> (
    <column 1 name> <data type for column 1>,
    <column 2 name> <data type for column 2>,
    <column 3 name> <data type for column 3>,
    ...
    <column N name> <data type for column N>
)
```

#### Change table name

`ALTER TABLE <table name> RENAME TO <new table name>`

#### Renaming a Column:

`ALTER TABLE <table name> RENAME COLUMN <existing column name> TO <new column name>;`

#### Adding New Columns

`ALTER TABLE <table name> ADD COLUMN <definition of your new column>` ex: dummy_column INT

#### View all columns in iPython:

```bash
cursor.execute("DESCRIBE Stock")

 result = cursor.fetchall()
    for row in result:
       print(row)
```

#### See each column

```bash
See each column
for row in result:
    print(row[0])

```

#### Drop a column

`ALTER TABLE <table name> DROP COLUMN <column name>;`

#### Adding Entries to Your Table

`INSERT INTO <table name> (<columns to enter data into>) VALUES` (<corresponding values for each column>)

#### Updating Values in Your Table

`UPDATE <table name> SET <column name> = <new value> WHERE <condition describing the row>`

#### Deleting Rows

`DELETE FROM <table name> WHERE <condition describing the row>`

#### SAVE CHANGES:

`conn.commit()`
`conn.close()`
