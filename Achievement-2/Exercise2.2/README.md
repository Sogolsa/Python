# Django Project Set Up

## Django Terminology

### Project and App

- A Django project is a complete application structure consisting of multiple modules (apps), configuration files, and a database. The project name is typically the name of the application
- A Django app is a module with specific functionality.

### Configuration Files and Database

- Configuration files manage an array of project functions. => allow basic Django admin functionality, such as creating databases and running the server on localhost.
- The database stores project data. By default, Django creates an SQLite3 database. => if you would like to use MySQL, specify in settings.py

## Creating a Django Project Structure

Step 1:

- Create a new virtual environment: `mkvirtualenv a2-ve-recipeapp`
- Activate virtual environment: `Envs\a2-ve-recipeapp\Scripts\activate.bat` for windows

Step 2:

- Install Django: `python -m pip install Django`

- Create a project inside the A2_Recipe_App directory: `django-admin.exe startproject <project_name>`
- Rename the recipe_project to src: To rename => make sure you are outside root directory (recipe_project)=> `rename recipe_project src` for windows cmd

Step 3:

- From within src folder: run migrations, run server
- To run migrations: inside src folder => `python manage.py migrate`
- To run the server on windows: `python manage.py runserver`

Step 4:

- Create superuser to access the admin panel: In src folder: `python manage.py createsuperuser`

- leave user name blank => take default user name
- email address optional
- Create a password:

Step 5: run the server
`python manage.py runserver`

- Log in to the Django site admin in localhost.
  http://127.0.0.1:8000/admin/ => login
