# Views and Templates

- A view is the logic that Django runs when a user accesses a URL.
- Each view is represented as a Python function, or as a method of a Python class that accepts a request, runs Python code, and returns a response.
- Every view is usually associated with a template, defining the output’s structure.
- Django selects the view based on the URL coming from the web application in the browser.
- To get from a URL to a view (and template), Django uses configurations that map URL patterns to views.

# Creating a Custom Welcome Page

1. Defining the view in the app/views.py file.
2. Creating the template(s) in the app/templates/ folder.
3. Mapping the URL to view in app/urls.py.
4. Registering the URL and view in project/urls.py.
