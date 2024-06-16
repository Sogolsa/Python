class Recipe:
    """Class to represent a recipe."""

    all_ingredients = set()

    def __init__(self, name):
        """Initialize the recipe with a name."""
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def get_name(self):
        """Return the name of the recipe."""
        return self.name

    def get_cooking_time(self):
        """Return the cooking time of the recipe."""
        return self.cooking_time

    def get_ingredients(self):
        """Return the ingredients of the recipe."""
        return self.ingredients

    def set_name(self, name):
        """Set the name of the recipe."""
        self.name = name

    def set_cooking_time(self, cooking_time):
        """Set the cooking time of the recipe."""
        if cooking_time < 0:
            raise ValueError("Cooking time can not be negative")
        self.cooking_time = cooking_time

    def add_ingredients(self, items):
        """Add ingredients to the recipe."""
        self.ingredients.extend(items)
        self.update_all_ingredients()

    def update_all_ingredients(self):
        """Update the class attribute with all unique ingredients."""
        Recipe.all_ingredients.update(self.ingredients)

    def calculate_difficulty(self):
        """Calculate and set the difficulty of the recipe."""
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10:
            self.difficulty = "Easy" if num_ingredients < 4 else "Medium"
        else:
            self.difficulty = "Intermediate" if num_ingredients < 4 else "Hard"

    def get_difficulty(self):
        """Return the difficulty of the recipe."""
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        """Return True if the ingredient is in the recipe, otherwise False."""
        return ingredient in self.ingredients

    def __str__(self):
        """Return a formatted string representation of the recipe."""
        ingredients_str = ", ".join(self.ingredients)
        return (
            f"\nRecipe Name: {self.name}\n"
            f"Cooking time (mins): {self.cooking_time}\n"
            f"Ingredients: {ingredients_str}\n"
            f"Difficulty: {self.get_difficulty()}\n"
        )


"""
data: takes in a list of Recipe objects to search from
search_term: the ingredient to be searched for
"""


def recipe_search(data, search_term):
    """Print recipes that contain the specified ingredient."""
    found = False
    print(f"Recipes that contain: {search_term}\n{'-' * 30}")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
            found = True
    if not found:
        print("No recipe found with that ingredient.")


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
print("Recipes list:")
print("-" * 30)
for recipe in recipes_list:
    print(recipe)

# Search recipes ingredients
for ingredient in ["Water", "Sugar", "Bananas"]:
    recipe_search(recipes_list, ingredient)
