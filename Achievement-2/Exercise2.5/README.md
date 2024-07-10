# Adding Support for User-Generated (Media) Images

1. Have a designated folder at the project (application) level where the images will be stored.
2. Specify the path to this image folder in the project’s settings.py file.
3. Specify URL-View mapping in the project’s urls.py file.
4. Add the pic attribute to model(s). Update the code in the models.py files of the individual apps to create new fields/columns in the database.
5. Provide a no-picture.jpg by default that the application can use in case an image isn’t available for a certain entity. This step is optional.

#### Tip:

Since you’ll be making changes to the models, remember that you need to keep running the commands makemigrations and migrate to implement these changes to the database.

## Step 1: Prepare Folder for Storing Images

- user-added images will be stored at the project (application) level. Done only once per project.
- create a folder called media under the src folder. (store your media files that are used globally in the project, including any defaults.)

## Step 2: Specify Path in Project’s settings.py File

- In main project directory => settings.py file (done once per project)
- Scroll down almost to the bottom of the file to the section on static files
- Below STATIC_URL, add the following parameters needed for media files. These correspond to user-generated content:

```bash
MEDIA_URL = '/media/'
MEDIA_ROOT= BASE_DIR / 'media'
```

## Step 3: Specify URL-View Mapping

- Include the media settings in urlpatterns
- In urls.py file at the project level
- Import settings (To access the MEDIA_URL and MEDIA_ROOT variables that you need to add) and static (provide access to the Django helper function static( ), which allows you to create URLs from local folder names.)

```bash
from django.conf import settings
from django.conf.urls.static import static
```

- Extend the urlpatterns parameter to include the media information.
  `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`

## Step 4: Add pic Attribute to Model

- Add a pic field to the model
- ### Step 4.1: Install the Python Package “Pillow”
- This package helps process images in Python and needs to be installed only once per project.
- To install this package, toggle the Terminal ON in VSCode. Next, ensure that your virtual environment is active
- `$pip install pillow`
- ### Step 4.2: Update Model to Add pic Attribute
- customers/model.py: `pic = models.ImageField(upload_to='customers', default='no_picture.jpg')`

## Step 5 (optional): Add no_picture.jpg as the Default

- using src/media (your global media folder) for your default files.
- Use the right path
- make migrations after changing the schema of the model:
- ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

# Adding Support for Developer-Generated (Static) Images

- Welcome view was created in recipes app
- Create a folder under recipes => static
- Create another folder under static => recipes
- Create a subfolder => images
- In recipes_home.html:
- To add image to html file: `load static` => generate the absolute URL of static files
- Next access the image from static folder
- Ask Django to load the static files for the HTML by adding the following line as the first line in the file:
  `{% load static %}` => tells Django to do something in particular before creating the complete HTML page from the template.
- After specifying the tag => open image by <img>
  `<img src="{% static 'recipes/images/home-background.jpg' %}" alt="home" width="600" height="300">`

# Accessing Records from the Database

- recipes app: create a page that lists the titles (making them clickable) and images of the recipes

1. Specifying all attributes in the Recipe model.
2. Entering recipe records in the database.
3. Creating the view and templates to display the list of recipes and registering the URLs with the app (recipes) and the project (recipe_project).

## Step 1: Specify Attributes in the Recipe Model

1. Have a designated folder where the images will be stored. This needs to be done once per project.
2. Specify the path to the folder in the project’s settings.py file. This also needs to be done once per project.
3. Specify URL-View mapping in the project’s urls.py file. This is a project-level entry and only needs to be done once per project.
4. (and 5): Update the code in the models.py files to create the attribute in the database. Also, provide the no_picture.jpg image by default. For this, add the following statement in your books/models.py file:

`pic = models.ImageField(upload_to='books', default='no_picture.jpg')`

- Activate virtual environment => run `python manage.py makemigrations` => `python manage.py migrate` => Run server

## Step 2: Add Recipes (Records) in the Database

- In the admin panel click add and add records

## Step 3: Specify View, Create Template, and Register URL

- Data is now in the database at the backend of your recipe-app application.

### Front end: 4 step process

1. Specify the View: recipes/views.py

- Import Django's ListView package (display data as a list)
- Import the Recipe Model(provides access to recipe records)
- Create a class based view(custom logic is not needed, generic functionality is good enough) => specify the model and template

2. Create Template:

- template is an HTML file that should be created in the recipes/templates/recipes folder
- create the recipes list first by accessing the model. Then, you’ll turn toward formatting and tabling.
- when the view executes, the model’s records are stored as a list in the variable called object_list(built-in variable)
- To access individual records within the object_list => loop through the list (for loop in recipes_list.html)
- Once you register your URL, you’ll be able to see your list of recipes
- Access recipe title and images: by {{object.name}} {{object.pic}}
- Specify the path to the image file (using {{object.pic.url}}) and then use the HTML image tag <img> to show the image

```bash
{% for object in object_list %}
   {{object.name}} - <img src="{{object.pic.url}}" width="150" height="200" />
   <br>
{% endfor %}
```

3. Map view to URL:

- create a new file: recipes/urls.py.
- To connect list/ with the RecipeListView (a class-based view), you need to call as_view() (a method of class ListView), which returns a callable view that takes a request and returns a response. as_view() => not needed for function based view

`urlpatterns = [path("recipes/", RecipeListView.as_view(), name="recipes")]`

4. Registering the View:

- recipe_project/urls.py

```bash
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('recipes.urls')),
]
```

# Creating Links Between Pages: Displaying Record Details

- Making recipe titles in the list clickable

## Step 1: Define the View:

- recipes/view.py => import django's DetailView package (display data details)
- Create a class based view => specify model and template

## Step 2: Create Template:

- recipes/templates/recipes => create recipes_detail.html

## Step 3: Map view to URL:

- create a link between the list page (that shows all recipes) and the details page of one recipe
- recipes/urls.py
- add `path('recipes/<pk>', RecipeDetailView.as_view(), name='detail')` to urlpatterns
- recipes/models.py => define get_absolute_url under Recipe class => takes <pk> as primary key and generates a URL
- Update recipes_list.html file: `<a href ="{{object.get_absolute_url}}"> {{object.name}} </a>` instead of {{object.name}}
  => to have recipe Titles as clickable links

# Adding Tests for Views and Templates

- recipes/test.py => def get_absolute_url(self) => `python manage.py test`
