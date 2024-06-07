# Initialize empty lists
recipes_list = []
ingredients_list = []

# Defining the function
def take_recipe():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = input("Enter the ingredients, separated by coma: ").split(", ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe

n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Hard'

for recipe in recipes_list:
    print("Recipe:", recipe['name'])
    print("Cooking Time (min):", recipe['cooking_time'])
    print("Ingredients:" )
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty level: " + recipe['difficulty'])

# Print all ingredients of all the recipes.
print("Ingredients Available Across All Recipes")
print("----------------------------------------")
 # Sort the ingredients alphabetically
ingredients_list.sort()
for ingredient in ingredients_list:
    print(ingredient)

