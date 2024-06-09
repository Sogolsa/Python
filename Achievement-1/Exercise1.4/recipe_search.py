import pickle

# Defining a function to display a recipe
def display_recipe(recipe):
    print('Recipe:', recipe['name'])
    print('Cooking Time (mins):', recipe['cooking_time'])
    print('Ingredients:')
    for ingredient in recipe['ingredients']:
       print(ingredient)   
    print('Difficulty:', recipe['difficulty'])
    

# Defining a function to search for an ingredient
def search_ingredient(data): 
    all_ingredients = data['all_ingredients']
    recipes_list = data['recipes_list']
    for position, ingredient in enumerate(all_ingredients):
        print('Ingredients ' + str(position) + ': ' + ingredient)
        
    try:
        ingredient_choice = int(input("Pick the number corresponding the ingredient you would like to search: "))
        ingredient_searched = all_ingredients[ingredient_choice]
    except ValueError:
        print('Invalid input. Please enter a valid number corresponding to the ingredient.')
    except IndexError:
        print('Invalid input. The selected ingredient number does not exist.')
    else:
        for recipe in recipes_list:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
    
# Main code, user input for the file containing recipe data
filename = input('Enter the filename where your recipes are stored (no extensions): ')

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print('File was not found.')
except:
    print('An unexpected error occurred.')
else:
    search_ingredient(data)
    

    