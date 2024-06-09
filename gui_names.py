

import tkinter as tk
from tkinter import ttk
from name_list import get_names_with_ages
from read_data import data_by_category
# Create the main window
root = tk.Tk()
root.title("Names and Ages List")

height = 3
width = 2

all_names = data_by_category()

keys = list(all_names.keys())

# print(keys[0])

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Time"), show="headings")

# Add column headings
tree.heading("Name", text="Name")
tree.heading("Time", text="Time")

# Get the list of names with ages
names_with_ages = get_names_with_ages()

# Insert data into the Treeview
all_names = data_by_category()

for name, category_only in all_names['open']:
    tree.insert("", "end", values=(name, category_only))

# Display the Treeview
tree.pack()
tree.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the Tkinter event loop
root.mainloop()