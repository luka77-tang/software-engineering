import tkinter as tk
from tkinter import messagebox

# Main application class
class RevivalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Item Revival Software")
        self.root.configure(bg="#f0f0f0")  # Background color

        # Item list to store item information
        self.items = []

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Label Styles
        label_style = {"font": ("Arial", 12), "bg": "#f0f0f0", "fg": "#333"}

        # Labels and Entries for input fields
        self.name_label = tk.Label(self.root, text="Item Name:", **label_style)
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(self.root, width=40, font=("Arial", 12), bd=2)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.desc_label = tk.Label(self.root, text="Item Description:", **label_style)
        self.desc_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.desc_entry = tk.Entry(self.root, width=40, font=("Arial", 12), bd=2)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=10)

        self.contact_label = tk.Label(self.root, text="Contact Info:", **label_style)
        self.contact_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.contact_entry = tk.Entry(self.root, width=40, font=("Arial", 12), bd=2)
        self.contact_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button Styles
        button_style = {"font": ("Arial", 12, "bold"), "fg": "white", "bd": 2, "width": 15}

        self.add_button = tk.Button(self.root, text="Add Item", bg="#4CAF50", **button_style, command=self.add_item)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Item", bg="#F44336", **button_style, command=self.delete_item)
        self.delete_button.grid(row=3, column=1, padx=10, pady=10)

        self.display_button = tk.Button(self.root, text="Display Items", bg="#2196F3", **button_style, command=self.display_items)
        self.display_button.grid(row=4, column=0, padx=10, pady=10)

        self.search_button = tk.Button(self.root, text="Search Item", bg="#FF9800", **button_style, command=self.search_item)
        self.search_button.grid(row=4, column=1, padx=10, pady=10)

        # Listbox to display items
        self.listbox = tk.Listbox(self.root, width=70, height=10, font=("Arial", 12), bd=2)
        self.listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Scrollbar for the Listbox
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.grid(row=5, column=2, sticky="ns")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

    def add_item(self):
        # Get user input
        name = self.name_entry.get()
        description = self.desc_entry.get()
        contact = self.contact_entry.get()

        # Check if input fields are empty
        if not name or not description or not contact:
            messagebox.showerror("Error", "All fields must be filled!")
            return

        # Add item to the list
        item = {"name": name, "description": description, "contact": contact}
        self.items.append(item)

        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Item added successfully!")

    def delete_item(self):
        # Get selected item from the listbox
        selected_item_index = self.listbox.curselection()
        if not selected_item_index:
            messagebox.showerror("Error", "Please select an item to delete.")
            return

        # Delete the selected item
        del self.items[selected_item_index[0]]
        self.listbox.delete(selected_item_index)

        messagebox.showinfo("Success", "Item deleted successfully!")

    def display_items(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)

        # Display all items in the listbox
        for item in self.items:
            self.listbox.insert(tk.END, f"Name: {item['name']}, Description: {item['description']}, Contact: {item['contact']}")

    def search_item(self):
        # Get the name to search for
        search_name = self.name_entry.get()

        if not search_name:
            messagebox.showerror("Error", "Please enter an item name to search.")
            return

        # Clear the listbox
        self.listbox.delete(0, tk.END)

        # Search for the item and display it
        found = False
        for item in self.items:
            if search_name.lower() in item['name'].lower():
                self.listbox.insert(tk.END, f"Name: {item['name']}, Description: {item['description']}, Contact: {item['contact']}")
                found = True

        if not found:
            messagebox.showinfo("Not Found", f"No items found with the name: {search_name}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RevivalApp(root)
    root.mainloop()
