import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from common.magic_item_properties import *
from common.common_methods import *
from config.config import *

def generate_magic_item():
    character_name = character_var.get()

    if (table_number_var.get() != ""):
        table_number = int(table_number_var.get())
        rarity = table_mapping[table_number]
    elif (table_d100_var.get() != ""):
        table_d100 = int(table_d100_var.get())
        rarity = determine_rarity_from_d100(table_d100)
    else:
        rarity = pick_random_rarity(rarities_probabilities)

    if ( row_number_var.get() == ""):
        magic_item_name = get_magic_item(rarity)
    else:
        row_number = int(row_number_var.get())
        magic_item_name = get_magic_item_from_table(table_number, row_number)

    magic_items_info = get_magic_items_from_file("data/magic_items_data.txt")

    notes = generate_item_notes(magic_item_name)
    item_price = get_item_price(rarity)
    magic_item_url = get_magic_item_url(magic_item_name, magic_items_info)
    rarity_text = get_xlation(rarity)
    emoticons = get_emoticons(rarity)

    output_text = f"**{character_name} found an item!**\n"
    output_text += f"{emoticons}\n"
    output_text += f"```\n"
    output_text += f"Item Name: {magic_item_name}\n"
    output_text += f"Rarity: {rarity_text}\n"
    if notes:
        output_text += f"{notes}\n"
    output_text += f"Gold Value: {item_price} gp\n"
    output_text += f"```\n"
    if magic_item_url:
        output_text += f"URL: <{magic_item_url}>\n"
        output_text += f"-----\n"
    else:
        print()
        output_text += f"\n!item {magic_item_name}"

    output_text_widget.delete(1.0, tk.END)
    output_text_widget.insert(tk.END, output_text)

# Create the main window
root = tk.Tk()
root.title("Magic Item Generator")

# Create and place widgets in the window
character_label = tk.Label(root, text="Select Character Name:")
character_label.pack()

character_var = tk.StringVar()
character_var.set(character_names[0])
character_menu = tk.OptionMenu(root, character_var, *character_names)
character_menu.pack()
character_menu.pack(pady=10)

table_number_label = tk.Label(root, text="Table Number (1-11):")
table_number_label.pack()

table_number_var = tk.StringVar()
table_number_entry = tk.Entry(root, textvariable=table_number_var)
table_number_entry.pack()
table_number_entry.pack(pady=10)

table_d100_label = tk.Label(root, text="1d100 roll:")
table_d100_label.pack()

table_d100_var = tk.StringVar()
table_d100_entry = tk.Entry(root, textvariable=table_d100_var)
table_d100_entry.pack()
table_d100_entry.pack(pady=10)

row_number_label = tk.Label(root, text="Row Number:")
row_number_label.pack()

row_number_var = tk.StringVar()
row_number_entry = tk.Entry(root, textvariable=row_number_var)
row_number_entry.pack()
row_number_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Magic Item", command=generate_magic_item)
generate_button.pack()

info_label = tk.Label(root, text=gui_info_text, justify=tk.LEFT, padx=10, pady=10, font=("Courier New", 10))
info_label.pack()

output_text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
output_text_widget.pack()

# Start the GUI event loop
root.mainloop()