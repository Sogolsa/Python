class Recipe:
    # Class attribute to store all unique ingredients across all instances of the Recipe class.
    all_ingredients = set()

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def get_name(self):
        return self.name

    def get_cooking_time(self):
        return self.cooking_time

    def get_ingredients(self):
        return self.ingredients

    # Setter method for name and cooking_time
    def set_name(self, name):
        self.name = name

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # Method to add ingredients
    def add_ingredients(self, items):
        self.ingredients.extend(items)
        self.update_all_ingredients()

    # Method for updating the all ingredients list
    def update_all_ingredients(self):
        for (
            ingredient
        ) in self.ingredients:  # For sets no need to check if there is no ingredient
            self.all_ingredients.add(ingredient)

    # Calculating the difficulty level of the recipe
    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = "Hard"

    # Getter method for difficulty, name, cooking_time and ingredients attributes
    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    # Method to search for an ingredient in the recipe and returns True or False
    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False

    # A string representation that prints the entire recipe over a well formatted string.
    def __str__(self):
        output = f"\nRecipe Name: {self.name}\nCooking_time(mins): {self.cooking_time}\nIngredients: {', '.join(self.ingredients)}\nDifficulty: {self.get_difficulty()}\n"
        return output


"""
data: takes in a list of Recipe objects to search from
search_term: the ingredient to be searched for
"""


# Method to find recipes that contain a specific ingredients
def recipe_search(data, search_term):
    found = False
    print(f"Recipes that contain: {search_term}\n...............................")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            found = True
    if not found:
        print("Recipe was not found")


# Creating Recipes
# Wrapping recipes in a recipe list
recipes_list = []

# Tea Recipe
tea = Recipe("Tea")
tea.add_ingredients(["Tea Leaves", "Sugar", "Water"])
tea.set_cooking_time(5)

recipes_list.append(tea)


# Coffee Recipe
coffee = Recipe("Coffee")
coffee.add_ingredients(["Coffee Powder", "Sugar", "Water"])
coffee.set_cooking_time(5)

recipes_list.append(coffee)


# Cake Recipe
cake = Recipe("Cake")
cake.add_ingredients(
    ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"]
)
cake.set_cooking_time(50)

recipes_list.append(cake)


# Banana Smoothie
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients(
    ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"]
)
banana_smoothie.set_cooking_time(5)

recipes_list.append(banana_smoothie)

# Print all the recipes
print("Recipes list: ")
print("................")
for recipe in recipes_list:
    print(recipe)

# Search recipes ingredients
for ingredient in ["Water", "Sugar", "Bananas"]:
    recipe_search(recipes_list, ingredient)
