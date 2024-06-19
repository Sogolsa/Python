# Connect to MySQL server
import mysql.connector  # type: ignore

# Initializing a connection object
conn = mysql.connector.connect(host="localhost", user="cf-python", passwd="password")

# Initializing a cursor object
cursor = conn.cursor()

# Create a Database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Access the database
cursor.execute("USE task_database")

# Create a table named Recipes
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Recipes (
    id    INT PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(50),
    ingredients    VARCHAR(255),
    cooking_time    INT,
    difficulty    VARCHAR(20)
)"""
)


# While loop to run the main menu
def main_menu(conn, cursor):
    choice = ""
    while choice != "quit":
        print("Main Menu\n" + "-" * 20)
        print("What would you like to do? Pick a choice!")
        print("1. Create a new recipe")
        print("2. Search for recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exist the program.")
        choice = input("\nYour Choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "quit":
            print("Exiting the program...")
            conn.commit()
            break
        else:
            print("Invalid choice, please try again!")


# Defining the create_recipe
def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")

    while True:
        try:
            cooking_time = int(
                input("Enter the cooking time of the recipe in minutes: ")
            )
            if cooking_time > 0:
                break
            else:
                print(
                    "Cooking time cannot be zero or negative. Please enter a valid positive integer."
                )
        except ValueError:
            print("Invalid input. Please enter a valid integer for cooking time.")

    # Ingredients as a list to easily calculate num_ingredients
    ingredients = input("Enter the ingredients, separated by coma: ").split(", ")
    difficulty = calc_difficulty(cooking_time, ingredients)

    # Back to string, since MySQL doesn't support list
    ingredients_str = ", ".join(ingredients)

    # Data entry into database
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print("Recipe was added successfully.\n")


def calc_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)
    if cooking_time < 10:
        difficulty = "Easy" if num_ingredients < 4 else "Medium"
    else:
        difficulty = "Intermediate" if num_ingredients < 4 else "Hard"

    return difficulty


# Display a single recipe
def show_recipe(recipe):
    print(f"\nRecipe Name: {recipe[1].title()}\n{'-' * 20}")
    print(f"Cooking Time: {recipe[3]} mins")
    print("Ingredients:")
    for ingredient in recipe[2].split(", "):
        print(f"  - {ingredient.title()}")
    print(f"Difficulty: {recipe[4]}\n")


# Fetch and display all recipes
def fetch_and_display_recipes(cursor):
    """Fetch all recipes from the database and display them nicely formatted."""
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    if len(results) == 0:
        print("No recipes found")
    else:
        print("Available Recipes:\n" + "-" * 20)
        for recipe in results:
            print(
                f"ID: {recipe[0]}\n"
                f"Recipe Name: {recipe[1]}\n"
                f"Cooking Time: {recipe[3]}\n"
                f"Ingredients: {recipe[2]}\n"
                f"Difficulty: {recipe[4]}\n"
            )
    return results


# Search recipes
def search_recipe(conn, cursor):
    """Retrieve all ingredients from Recipe table"""
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    if len(results) == 0:
        print("There are no recipes yet.\n")
        return

    """Extract unique ingredients"""
    all_ingredients = set()
    for row in results:
        """row[0] contains the ingredients string"""
        ingredients = row[0].split(", ")
        for ingredient in ingredients:
            if ingredient:  # Ensure the ingredient is not an empty string
                all_ingredients.add(ingredient)
    all_ingredients = list(all_ingredients)

    if not all_ingredients:
        print("No ingredients found in the database.")
        return

    # Prompt the user to pick from a list of ingredients
    print("Available ingredients:")
    for position, ingredient in enumerate(all_ingredients):
        print(f"Ingredient {position}: {ingredient}")

    while True:
        try:
            user_choice = int(
                input(
                    "Enter the number corresponding to the ingredient to search for: "
                )
            )
            if 0 <= user_choice < len(all_ingredients):
                search_ingredient = all_ingredients[user_choice]
                break
            else:
                print("Invalid choice. Please enter a number within the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except:
            print("An unexpected error occurred.\n")

    sql = "SELECT * FROM Recipes WHERE ingredients Like %s"
    val = f"%{search_ingredient}%"
    cursor.execute(sql, (val,))
    search_results = cursor.fetchall()
    if not search_results:
        print(f"No recipes found containing the ingredient '{search_ingredient}'.")
    else:
        for recipe in search_results:
            show_recipe(recipe)


# Update recipe
def update_recipe(conn, cursor):
    """Fetch and display all the recipes from database"""
    results = fetch_and_display_recipes(cursor)

    # Prompt the user to select recipe by ID
    while True:
        try:
            recipe_id = int(input("Enter the ID of the recipe you want to update: "))
            if any(recipe[0] == recipe_id for recipe in results):
                break
            else:
                print("Invalid ID. Please enter an ID from the list.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")
        except:
            print("An unexpected error occurred.\n")

    # Prompt the user to pick a column to update
    print(
        "Which column would you like to update\n"
        "1. name\n"
        "2. cooking_time\n"
        "3. ingredients\n"
    )

    while True:
        try:
            column_choice = int(input("Enter the number corresponding to the column: "))
            if column_choice in [1, 2, 3]:
                break
            else:
                print(
                    "Invalid number. Please select 1 for name, 2 for cooking_time, 3 for ingredients"
                )
        except ValueError:
            print("Invalid Input. Enter a number.")
        except:
            print("An unexpected error occurred.\n")

    # Collect new value from user
    if column_choice == 1:
        new_value = input("Enter new name: ")
        column_name = "name"
        sql = f"UPDATE Recipe SET {column_name} = %s WHERE id = %s"
        val = (new_value, recipe_id)
        cursor.execute(sql, val)
        print("The name was successfully updated.")
    elif column_choice == 2:
        while True:
            try:
                new_value = int(input("Enter new cooking time in minutes: "))
                if new_value > 0:
                    break
                else:
                    print("Cooking time must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        column_name = "cooking_time"
        sql = f"UPDATE Recipes SET {column_name} = %s WHERE id = %s"
        val = (new_value, recipe_id)
        cursor.execute(sql, val)

        # Recalculate difficulty
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients = cursor.fetchone()[0].split(", ")
        difficulty = calc_difficulty(new_value, ingredients)
        sql = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
        val = (difficulty, recipe_id)
        cursor.execute(sql, val)
        conn.commit()
        print("Recipe updated successfully.")

    elif column_choice == 3:
        new_value = input("Enter new ingredients, separated by commas: ").split(", ")
        column_name = "ingredients"
        new_value_str = ", ".join(new_value)
        sql = f"UPDATE Recipes SET {column_name} = %s WHERE id = %s"
        val = (new_value_str, recipe_id)
        cursor.execute(sql, val)

        # Recalculate difficulty
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        difficulty = calc_difficulty(cooking_time, new_value)
        sql = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
        val = (difficulty, recipe_id)
        cursor.execute(sql, val)
        conn.commit()
        print("Recipe updated successfully.")


# Delete a recipe
def delete_recipe(conn, cursor):
    results = fetch_and_display_recipes(cursor)

    try:
        recipe_id = int(input("Enter the ID of the recipe you want to delete: "))
        if any(recipe[0] == recipe_id for recipe in results):
            cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
            conn.commit()
            print("Recipe successfully deleted.")
        else:
            print("Invalid ID. Please enter an ID from the list.")
    except ValueError:
        print("Invalid Input. Please enter a valid number.")
    except:
        print("An unexpected error occurred.\n")


main_menu(conn, cursor)
conn.close()
