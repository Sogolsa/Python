# Creating a class
class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    # Methods to add and remove items
    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"{item} has been added to the shopping list!")
        else:
            print(f"{item} already exists!")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"{item} removed from the shopping list!")
        else:
            print(f"{item} does not exist in the shopping list!")

    def view_list(self):
        if not self.shopping_list:
            print("The shopping list is empty.")
        else:
            print(f"{self.list_name}:")
            for item in self.shopping_list:
                print(f"{item}")


pet_store_list = ShoppingList("Pet Store Shopping List")

pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")

pet_store_list.remove_item("flea collars")

pet_store_list.add_item("frisbee")

pet_store_list.view_list()
