# Item Revival Software

Designer: Tang Zhuohao 

Date: 2024/11/11

**Item Revival Software** is a Python application designed to help university students manage items they find valuable but no longer need or want to keep. This software allows users to add, display, delete, and search for items by storing each item's information in a user-friendly interface.

The application is built using the `tkinter` library, providing a simple GUI with labeled input fields and interactive buttons for ease of use.

---

## Features

1. **Add Item** - Allows users to enter an item's name, description, and contact information for future reference.
2. **Delete Item** - Enables the removal of an item from the list.
3. **Display Items** - Shows all added items in a list for easy reference.
4. **Search Item** - Searches for an item by its name and displays details if found.

## Requirements

- Python 3.x
- `tkinter` (This library comes pre-installed with Python for most distributions)

## Usage

### Getting Started

1. **Clone the repository** or copy the `RevivalApp` code into a Python file.
2. Run the Python file to launch the application.

```bash
python revival_app.py
```

### Interface Overview

Once the application is launched, a window with labeled fields and buttons will appear. Here’s how to use each feature:

### 1. Adding an Item

- Fill in the fields **Item Name**, **Item Description**, and **Contact Info**.
- Click the **Add Item** button.
- If all fields are filled in, the item will be added to the internal list and a success message will appear.
- If any field is left empty, an error message will prompt you to complete all fields.

### 2. Deleting an Item

- Select an item from the list displayed in the main window by clicking on it.
- Click the **Delete Item** button.
- The selected item will be removed from the list, and a success message will confirm the deletion.
- If no item is selected, an error message will appear asking you to select an item first.

### 3. Displaying Items

- Click the **Display Items** button to see all items stored in the list.
- The list of items will be displayed in the list box below the buttons, showing each item's name, description, and contact information.

### 4. Searching for an Item

- Enter the name of the item you wish to search for in the **Item Name** field.
- Click the **Search Item** button.
- If an item with the entered name (or part of the name) is found, it will be displayed in the list box.
- If no items match the search term, a message will inform you that no items were found.

## Code Structure

### RevivalApp Class

The primary class, `RevivalApp`, handles all functionalities of the Item Revival Software.

- `__init__(self, root)`: Initializes the main window and calls `create_widgets()` to build the GUI.
- `create_widgets(self)`: Defines and places all the UI elements (buttons, labels, entry fields, etc.) on the window.
- `add_item(self)`: Adds a new item to the internal list and clears the input fields.
- `delete_item(self)`: Deletes the selected item from the list and updates the display.
- `display_items(self)`: Shows all stored items in the list box.
- `search_item(self)`: Searches for an item by name and displays it if found.

### UI Components

Each button and label has its own style, with color-coding to help visually distinguish actions:

- **Add Item** button: Green background (`#4CAF50`), used for adding items.
- **Delete Item** button: Red background (`#F44336`), used for removing selected items.
- **Display Items** button: Blue background (`#2196F3`), used to show all items.
- **Search Item** button: Orange background (`#FF9800`), used for searching items by name.

### Examples

1. **Add an Item**

    - Enter:
      - `Item Name`: "Laptop Stand"
      - `Item Description`: "Adjustable height, good condition."
      - `Contact Info`: "jane.doe@example.com"
    - Click **Add Item**.
    - The item will be added to the internal list and displayed when you click **Display Items**.

2. **Delete an Item**

    - Select "Laptop Stand" from the displayed list.
    - Click **Delete Item**.
    - The item will be removed from the list.

3. **Search for an Item**

    - Enter `Item Name`: "Laptop Stand"
    - Click **Search Item**.
    - If the item exists, it will appear in the list box. If not, a message will display that no items were found.

---

## License

This project is open-source, and you are free to modify it for personal use. If you make improvements, please consider contributing back to the project.

## Acknowledgements

Thank you for using the Item Revival Software. We hope it makes it easier for you to manage items you find valuable but don't currently need.
