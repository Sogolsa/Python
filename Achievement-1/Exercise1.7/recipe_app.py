# Necessary Imports
from sqlalchemy import create_engine  # for connecting sqlalchemy to database
from sqlalchemy.orm import declarative_base  # For additional properties
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_


# Connecting Connecting SQLAlchemy with Database
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Generate the class from function
Base = declarative_base()

# Connection to the new engine with sessionmaker
Session = sessionmaker(bind=engine)

# Initialize the session object
session = Session()


class Recipe(Base):
    """Creating the table on database"""

    __tablename__ = "final_recipes"

    # Define table's attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(225))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        """repr method to show a quick representation of the recipe"""
        return (
            f"<Recipe ID: {self.id}, Name: {self.name}, Difficulty: {self.difficulty}>"
        )

    def __str__(self):
        """str method to print a well-formatted version of recipe"""
        return (
            f"\nRecipe Name: {self.name}\n"
            f"{'-' * 15}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}"
        )

    def calculate_difficulty(self):
        """Calculate the difficulty of the recipe, based on cooking time and ingredients."""
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10:
            self.difficulty = "Easy" if num_ingredients < 4 else "Medium"
        else:
            self.difficulty = "Intermediate" if num_ingredients < 4 else "Hard"

    def return_ingredients_as_list(self):
        """Retrieve the ingredients string as a list"""
        if self.ingredients == "":
            return []
        else:
            return self.ingredients.split(", ")


Base.metadata.create_all(engine)


def create_recipe():
    """Collect details of recipe from user"""

    # Collecting name
    while True:
        name = input("Enter the name of the recipe (Max 50 characters): ")
        if len(name) > 50:
            print("Error: name cannot exceed 50 characters.")
        elif not name.replace(" ", "").isalnum():
            print("Error: Name must contain only alphanumeric characters.")
        else:
            break

    # Collecting cooking time
    while True:
        cooking_time = input("Enter the cooking time in minutes: ")
        if not cooking_time.isnumeric():
            print("Error: cooking time must be a number.")
        else:
            cooking_time = int(cooking_time)
            if cooking_time <= 0:
                print("Error: cooking time must be a positive number.")
            else:
                break

    # Collecting ingredient
    ingredients_set = set()
    while True:
        try:
            num_ingredients = int(
                input("Enter the number of ingredients for this recipe: ")
            )
            if num_ingredients <= 0:
                print("Error: number of ingredients must be a positive number.")
            else:
                break
        except ValueError:
            print("Error: number of ingredients must be a number.")

    for _ in range(num_ingredients):
        ingredient = input("Enter an ingredient: ")
        ingredients_set.add(ingredient)

    ingredients = ", ".join(ingredients_set)

    recipe_entry = Recipe(name=name, ingredients=ingredients, cooking_time=cooking_time)

    # Generating the difficulty attribute
    recipe_entry.calculate_difficulty()

    # Adding the recipe to the session and committing the change
    session.add(recipe_entry)
    session.commit()
    print("Recipe added successfully!\n")


def view_all_recipes():
    """Retrieve all recipes from the database and display them."""

    # Retrieve all recipes
    recipes = session.query(Recipe).all()

    # Check if there are no recipes
    if not Recipe:
        print("There are no recipes in the database.")
        return None

    # Loop through recipes and display them
    for recipe in recipes:
        print(recipe)


def search_by_ingredient():
    """Search for recipes based on ingredients provided by the user."""

    # Check if there are any entries in database
    num_entries = session.query(Recipe).count()
    if num_entries == 0:
        print("There no entries in the database.")
        return None

    # Retrieve ingredients
    results = session.query(Recipe.ingredients).all()

    # Initialize empty set of ingredients
    all_ingredients = set()

    # Collect all unique ingredients from the database
    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            all_ingredients.add(ingredient)
    all_ingredients = list(all_ingredients)

    # Display all ingredients with numbers
    print("Available ingredients to search for recipes:\n" + "-" * 45)
    for position, ingredient in enumerate(all_ingredients):
        print(f"Ingredient {position}: {ingredient}")

    # Ask user for ingredients to search by
    while True:
        try:
            user_choice = input(
                "Enter number corresponding the ingredient to search for, separated by spaces: "
            ).split(" ")
            search_ingredients = []
            for choice in user_choice:
                user_choice = int(choice)
                search_ingredients.append(all_ingredients[user_choice])
        except ValueError:
            print("\nOne or more of your inputs aren't numbers.\n")
            return
        except IndexError:
            print("\nThe number you chose is not in the list.\n")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

        conditions = []
        for ingredient in search_ingredients:
            like_term = f"%{ingredient}%"
            conditions.append(Recipe.ingredients.like(like_term))

        recipes = session.query(Recipe).filter(*conditions).all()
        if len(recipes) <= 0:
            print("No recipes found containing the selected ingredients.")
        else:
            print("Recipes found containing the selected ingredients: ")
            for recipe in recipes:
                print(recipe)


def edit_recipe():
    """Edit an existing recipe in the database."""

    # Check if there are any recipes in the database
    num_recipes = session.query(Recipe).count()
    if num_recipes == 0:
        print("There are no entries in the database.")
        return None

    # Retrieve the id and name of each recipe
    results = session.query(Recipe.id, Recipe.name).all()

    # Display the available recipes to the user
    print("Available Recipes:\n" + "-" * 20)
    for recipe in results:
        print(f"\nID: {recipe.id} - Name: {recipe.name}\n")

    # Ask the user to pick a recipe by its id
    while True:
        try:
            selected_id = int(
                input("Enter the ID of the recipe you would like to edit: ")
            )
            if selected_id not in [recipe.id for recipe in results]:
                print("Invalid ID was selected.")
                continue
            break
        except ValueError:
            print("Invalid input. Please select a valid number.")
        except:
            print("An unexpected error has occurred.")

    # Retrieve the recipe corresponding with id
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == selected_id).one()

    if recipe_to_edit is None:
        print("Error: Recipe with the specified ID does not exist.")
        return None

    # Display recipe
    print(
        f"\nRecipe to be edited:\n"
        f"1. Name: {recipe_to_edit.name}\n"
        f"2. Ingredients: {recipe_to_edit.ingredients}\n"
        f"3. Cooking Time: {recipe_to_edit.cooking_time} minutes\n"
    )

    # Ask user which attribute to edit
    while True:
        try:
            selected_attribute = int(
                input(
                    "Enter the number corresponding to the attribute you would like to edit: "
                )
            )
            if selected_attribute not in [1, 2, 3]:
                print(
                    "Error: Invalid number. Please enter 1 for Name, 2 for Ingredients or 3 for Cooking Time."
                )
                continue
            break
        except ValueError:
            print("Invalid Input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

    if selected_attribute == 1:
        new_name = input("Enter the new name for the recipe: ")
        if len(new_name) > 50:
            print("Error: Name can not exceed 50 characters.")
        elif not new_name.replace(" ", "").isalnum():
            print("Error: Name must contain only alphanumeric characters.")
        else:
            recipe_to_edit.name = new_name
    elif selected_attribute == 2:
        new_ingredients = input("Enter the new ingredients (comma separated): ")
        recipe_to_edit.ingredients = new_ingredients
    elif selected_attribute == 3:
        while True:
            try:
                new_cooking_time = int(input("Enter new cooking time in minutes: "))
                if new_cooking_time > 0:
                    recipe_to_edit.cooking_time = new_cooking_time
                    break
                else:
                    print("Cooking time must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"An unexpected Error occurred: {e}")

    # Recalculate the difficulty
    recipe_to_edit.calculate_difficulty()

    # Commit these changes to the database
    session.commit()
    print("Recipe updated successfully.")


def delete_recipe():
    """Deleting an existing recipe."""
    try:
        # Check if any recipe exists
        num_recipes = session.query(Recipe).count()
        if num_recipes == 0:
            print("No recipe available in database.")
            return None

        """Retrieve recipe by id and name"""
        results = session.query(Recipe.id, Recipe.name).all()

        """Display Recipes available"""
        print("Available Recipes:\n" + "-" * 30)
        for recipe in results:
            print(f"\nID: {recipe.id} - Name: {recipe.name}\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    """Ask user to pick a recipe by its id"""
    while True:
        try:
            selected_id = int(
                input("Enter the ID of the recipe you would like to delete: ")
            )
            if selected_id not in [recipe.id for recipe in results]:
                print("Invalid ID. Please select the right ID.")
                continue
            if selected_id <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid Input. Please select a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    """Retrieve the corresponding recipe object from the database"""
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == selected_id).one()
    if not recipe_to_delete:
        print("Recipe not found.")
        return None

    """Ask the user for confirmation"""
    confirmation = input(
        f"\nAre you sure you want to delete the recipe `{recipe_to_delete.name}`? (yes/no): "
    )
    if confirmation.lower() != "yes":
        print("Recipe was not deleted!")
        return

    """Delete operation and commit changes"""
    session.delete(recipe_to_delete)
    session.commit()
    print("\nRecipe deleted successfully.")


def main_menu():
    choice = ""
    while choice != "quit":
        print("Main Menu\n" + "-" * 20)
        print("What would you like to do? Pick a choice!")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipe by ingredient")
        print("4. Edit an existing recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exist the program.")
        choice = input("\nYour Choice: ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredient()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("Exiting the program.")
            break
        else:
            print("Invalid Choice! Please try again!")


if __name__ == "__main__":
    main_menu()

    Session.close_all()
    engine.dispose()
