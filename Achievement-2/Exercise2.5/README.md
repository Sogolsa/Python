# Adding Support for User-Generated (Media) Images

1. Have a designated folder at the project (application) level where the images will be stored.
2. Specify the path to this image folder in the project’s settings.py file.
3. Specify URL-View mapping in the project’s urls.py file.
4. Add the pic attribute to model(s). Update the code in the models.py files of the individual apps to create new fields/columns in the database.
5. Provide a no-picture.jpg by default that the application can use in case an image isn’t available for a certain entity. This step is optional.

#### Tip:

Since you’ll be making changes to the models, remember that you need to keep running the commands makemigrations and migrate to implement these changes to the database.
