import pickle


# Defining a function to take the recipe from the users and return recipe information with difficulty level
def take_recipe():
    name = input("Enter the name of the recipe: ")
    while True:
        try:
            cooking_time = int(input("Enter cooking time in minutes: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for cooking time.")
    ingredients = input("Enter the ingredients, separated by coma: ").split(", ")
    num_ingredients = len(ingredients)
    difficulty = calc_difficulty(cooking_time, num_ingredients)
    return {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }


# Defining a function to calculate the difficulty level
def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        difficulty = "Hard"

    return difficulty


# Main code to get the recipe file from the user
filename = input("Enter file name to load recipes from: ")

# Open the given file and loads the content through pickle module
try:
    with open(filename, "rb") as file:
        data = pickle.load(file)

# Handling errors where the given file is not found
except FileNotFoundError:
    print("File not found, creating a new file")
    data = {
        "recipes_list": [],
        "all_ingredients": set(),  # Efficiency in Checking duplicates
    }

# Handling any other errors that occurs
except:
    print("An error occurred, creating a new file")
    data = {"recipes_list": [], "all_ingredients": set()}
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

# User input on how many recipes they would like to enter
while True:
    try:
        num_recipes = int(input("How many recipes would you like to enter? "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# For loop to call the take_recipe() function
for i in range(num_recipes):
    new_recipe = take_recipe()
    recipes_list.append(new_recipe)
    for ingredient in new_recipe["ingredients"]:
        # if ingredient not in all_ingredients:
        all_ingredients.add(ingredient)  # Using add for set

# Gather updated data with new recipes list and ingredients list
data["recipes_list"] = recipes_list
data["all_ingredients"] = list(
    all_ingredients
)  # convert to list for broader compatibility

# Save data in binary file
saved_filename = input("Enter file name to save recipes to: ")
with open(saved_filename, "wb") as file:
    pickle.dump(data, file)
