# Django Models

- Models are Python objects that Django web applications use to access and manage data from the database. Django models define the structure of the data stored in the database, including field types, default values, the maximum size of the stored data, and so on.
- The next layers of the process (the VT of MVT) will be based off of the model (M). Changes to the model at later stages are time-consuming and may even cause the app to break.

## Database blueprint

A database blueprint is a rough outline of the database and its planned structure. Creating a blueprint is useful as it allows the creator to gain a better understanding of each app’s attributes, relationships, and even constraints.

## Django App Creation Per Application Requirements

- In src folder: `python manage.py startapp <app name>`
