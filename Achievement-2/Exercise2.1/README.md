# Getting Started with Django

- Explain MVT architecture and compare it with MVC
- Summarize Django’s benefits and drawbacks
- Install and get started with Django

## Model View Template (MVT) Architecture

- Model: Helps handle an application’s data and implement the functionality related to the database. The Model can retrieve, update, and delete records from the database.
- View: Takes care of the application’s business logic and acts as an interface between the Model and Template. View takes the data from the Model and renders it on the Template.
- Template: Handles the user interface and takes care of the presentation. The Template also determines how the output should be structured for the browser.

### Django’s Benefits

- Fast Development:
- Fast Processing
- DRY (Don't repeat yourself principle)
- Support for Content Delivery Networks and Content Management
- Scalability
- Security
- Community

# Preparing for Installation

### Install the following three pieces of software:

- Python
- Virtual Environment => refer to Achievement-1, Exercise1.1 of this repository for installation
- Visual Studio Code

## Getting Started with Django:(on Windows)

1. Step 1: Create virtual environments named `web-dev`

- Manage virtual environments via `virtualenvwrapper-win` extension
- Make new virtual environment: (command prompt)
  `mkvirtualenv web-dev`
  will be stored by default in C:\Users\<username>\Envs directory

2. Step 2: Install Django

- command prompt
- Check if your virtual environment is active:
  `web-dev\Scripts\activate.bat`
- Install Django:
  `py -m pip install Django` => If it doesn't work use python instead of py
  verify Django installation: `django-admin --version`
