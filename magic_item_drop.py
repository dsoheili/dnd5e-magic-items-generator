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

    if (row_number_var.get() == ""):
        magic_item_name = get_magic_item(rarity)
    else:
        row_number = int(row_number_var.get())
        magic_item_name = get_magic_item_from_table(rarity, row_number)

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

root = tk.Tk()
root.title("Magic Item Generator")
root.geometry("600x400")  # Adjust the size as needed

# Use frames for better organization
input_frame = ttk.Frame(root, padding="10 10 10 10")
input_frame.pack(fill=tk.BOTH, expand=True)

output_frame = ttk.Frame(root, padding="10 10 10 10")
output_frame.pack(fill=tk.BOTH, expand=True)

# Style the components
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 10), padding=10)
style.configure('TLabel', font=('Helvetica', 10), padding=5)
style.configure('TEntry', font=('Helvetica', 10), padding=5)

# Input fields
character_label = ttk.Label(input_frame, text="Select Character Name:")
character_label.grid(column=0, row=0)

character_var = tk.StringVar()
character_menu = ttk.OptionMenu(input_frame, character_var, None, *character_names)  # Removed inappropriate style
character_menu.grid(column=1, row=0, sticky=tk.EW)

table_number_label = ttk.Label(input_frame, text="Table Number (1-11):")
table_number_label.grid(column=0, row=1)

table_number_var = tk.StringVar()
table_number_entry = ttk.Entry(input_frame, textvariable=table_number_var)
table_number_entry.grid(column=1, row=1, sticky=tk.EW)

table_d100_label = ttk.Label(input_frame, text="1d100 roll:")
table_d100_label.grid(column=0, row=2)

table_d100_var = tk.StringVar()
table_d100_entry = ttk.Entry(input_frame, textvariable=table_d100_var)
table_d100_entry.grid(column=1, row=2, sticky=tk.EW)

row_number_label = ttk.Label(input_frame, text="Row Number:")
row_number_label.grid(column=0, row=3)

row_number_var = tk.StringVar()
row_number_entry = ttk.Entry(input_frame, textvariable=row_number_var)
row_number_entry.grid(column=1, row=3, sticky=tk.EW)

generate_button = ttk.Button(input_frame, text="Generate Magic Item", command=generate_magic_item)
generate_button.grid(column=0, row=4, columnspan=2, pady=10)

# Output area
output_text_widget = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=50, height=10, font=('Helvetica', 11))
output_text_widget.pack(fill=tk.BOTH, expand=True)

root.mainloop()