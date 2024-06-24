# Object-Relational Mapping in Python

ORM makes database conversion much easier, especially when moving from one DBMS to another

## SQLAlchemy

an open-source Python SQL toolkit to implement ORM. SQLAlchemy comes with many tools for managing the interface between application and database.

### Setting up SQLAlchemy

- Step 1
  Open a terminal => activate a virtual environment
  `pip install sqlalchemy`
- Step 2
  Install the connector package that SQLAlchemy can use
  `pip install mysqlclient`

  If any issues when installing mysqlclient, install mysql via Homebrew first:
  `brew install mysql`

  ## Checking MySQL Server is Running

  Before starting to work on SQLAlchemy, make sure that your MySQL server is running in the background. To do so for windows:

- MySQL for windows:
  In Windows, MySQL runs as a service:

1. Press Windows + R
2. Type: services.msc
3. Scroll down and find MYSQL80
4. Double click to see its properties
5. Service Status: Running
6. If service status is not running => Click Start button

## Connecting SQLAlchemy with Your Database

1. Open an iPython shell
2. Import create_engine function from sqlalchemy
   `from sqlalchemy import create_engine`
   The create_engine function lets you connect to your database through a URL in the following format:
   `<database type>://<username>:<password>@<hostname>/<database name>`
   Wrap it around create_engine function:
   `engine = create_engine("mysql://cf-python:password@localhost/my_database")`

#### Creating a Table from a Mapped Class

- To map the classes to table on database through SQLAlchemy, declaring a regular class is not enough.
- Additional properties coming from a special class in SQLAlchemy known as a declarative base, needs to be inherited.
- `from sqlalchemy.ext.declarative import declarative_base`
- Generate the class from function:
  `Base = declarative_base()`

#### To create a representation of this table as a class:

- import a couple of types that SQLAlchemy offers
  `from sqlalchemy import Column`
  `from sqlalchemy.types import Integer, String`
- Declare a new class, inheriting properties from Base
- Declaring table name is optional, if it's not declared, table name will be class name

```bash
class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
```

- Recipe is a data model that stores the representation of the table’s structure in the database.

- Use the create_all() method in the base class to create tables of all the models that you’ve defined: `Base.metadata.create_all(engine)`
- To check the table, open the command line interface for MySQL
- Type the following mysql> commands: (MySQL command line)

```bash
USE my_database
SHOW TABLES;
```

- To look at internal structure
  `DESCRIBE practice_recipes;`

#### Creating a Session for Your Database

handles a connection to the new engine. With this, you’ll be able to change the database’s contents using an OOP approach rather than SQL queries.
Add entries to table as objects from the class.

1. `from sqlalchemy.orm import sessionmaker`
2. `Session = sessionmaker(bind=engine)`
3. Initialize the session object: `session = Session()`

#### Adding Entries to Table

Class/Model => Create objects => Add object to database => Commit the entry
`session.add(object name)`
`session.commit()`

#### Reading Entries from a Table

`query(<class/model name>)`
`session.query(Recipe).all()` => Retrieves everything from the table as a list of objects

- Retrieving a Single Object Using the get() Method
  `session.query(class).get(primary_key)`
- Retrieving One or More Objects Using the filter() Method
  If not sure of the primary_key you are looking for
  `session.query(<model name>).filter(<model name>.<attribute/column name> == <value to compare against>).one()`

  - Using the like() Method
    search for bits of strings or patterns in the row

#### Updating Entries in Your Table

1. Retrieve objects from table
2. Edit the necessary attribute(s) in an object
3. Commit your changes

#### Making Direct Changes Using the update() Method for multiple rows

```bash
session.query(<model name>).filter(<column 1 name> == 'value for column 1').update({<model name>.<column 1 name> : <new value for column 1>})
session.commit()
```

#### Deleting Entries from Your Table

```bash
table_to_be_deleted = session.query(<model name>).filter(<column 1 name == <value for column 1>).one()
session.delete(table_to_be_deleted)
session.commit()
```

#### Bringing out both the 'column 1' and 'column 2' from our table

- with_entities
  `session.query(<model name>).with_entities(column 1, column 2).all()`
