class RevivalApp:
    def __init__(self):
        self.items = []

    def display_items(self):
        if not self.items:
            print("No items found.")
        else:
            print("Current items:")
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. Name: {item['name']}, Description: {item['description']}, Contact: {item['contact']}")

    def add_item(self):
        while True:
            name = input("Enter item name (or type 'back' to return to menu): ")
            if name.lower() == 'back':
                return

            # Allow modification of description
            while True:
                description = input("Enter item description (or type 'edit' to modify name or 'back' to return to menu): ")
                if description.lower() == 'back':
                    return
                if description.lower() == 'edit':
                    break  # Return to input name

                if not description:
                    print("Description can't be empty!")
                    continue

                # Allow modification of contact info
                while True:
                    contact = input("Enter contact info (or type 'edit' to modify description or 'back' to return to menu): ")
                    if contact.lower() == 'back':
                        return
                    if contact.lower() == 'edit':
                        break  # Return to input description

                    if not contact:
                        print("Contact info can't be empty!")
                        continue

                    # If all inputs are valid, add the item
                    item = {"name": name, "description": description, "contact": contact}
                    self.items.append(item)
                    print("Item added successfully!")
                    return

    def delete_item(self):
        while True:
            self.display_items()
            try:
                index = input("Enter the number of the item to delete (or type 'back' to return to menu): ")
                if index.lower() == 'back':
                    return

                index = int(index) - 1
                if index < 0 or index >= len(self.items):
                    print("Invalid number!")
                    continue

                del self.items[index]
                print("Item deleted successfully!")
                return
            except ValueError:
                print("Please enter a valid number!")

    def search_item(self):
        while True:
            search_name = input("Enter item name to search (or type 'back' to return to menu): ")
            if search_name.lower() == 'back':
                return

            if not search_name:
                print("Please enter an item name to search!")
                continue

            found = False
            for item in self.items:
                if search_name.lower() in item['name'].lower():
                    print(f"Found item: Name: {item['name']}, Description: {item['description']}, Contact: {item['contact']}")
                    found = True

            if not found:
                print(f"No items found with the name containing: {search_name}.")
            return

# Main loop
if __name__ == "__main__":
    app = RevivalApp()

    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Delete Item")
        print("3. Display Items")
        print("4. Search Item")
        print("5. Exit Program")
        print("Type 'back' at any prompt to return to the menu.")

        choice = input("Select an action: ")

        if choice == '1':
            app.add_item()
        elif choice == '2':
            app.delete_item()
        elif choice == '3':
            app.display_items()
        elif choice == '4':
            app.search_item()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid option, please try again.")