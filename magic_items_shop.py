import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from common.magic_item_properties import *
from common.common_methods import *
from config.config import *

url_data = get_magic_items_from_file("data/magic_items_data.txt")

def stock_shop_shelf():
    items_without_url = []
    output_text = ""

    for i in range(number_of_shop_items):
        if random_rarities_for_shop_items:
            rarity = pick_random_rarity()
        else:
            if i < len(shop_items_predefined_rarities):
                rarity = random.choice(shop_items_predefined_rarities[i])
            else:
                rarity = default_shop_rarity

        rarity_text = get_xlation(rarity)
        magic_item_name = get_magic_item(rarity)
        item_price = get_item_price(rarity)
        notes = generate_item_notes(magic_item_name)
        magic_item_url = get_magic_item_url(magic_item_name, url_data)

        enchanted = None
        if magic_item_enchantments_enabled:
            enchanted, enchantment_effect = determine_enchantment()

        output_text += f"### {magic_item_name}\n"
        output_text += f"*{rarity_text}*\n"
        output_text += f"Price: {item_price:,} GP\n"

        if notes != "":
            output_text += f"{notes}\n"

        if enchanted:
            output_text += f"**{enchanted}** - {enchantment_effect}\n"

        if magic_item_url:
            output_text += f"<{magic_item_url}>\n"
        else:
            items_without_url.append(magic_item_name)

        output_text += "\n"

    output_text += "\n"
    for magic_item in items_without_url:
        output_text += f"!item {magic_item}\n"

    output_text_widget.delete(1.0, tk.END)
    output_text_widget.insert(tk.END, output_text)

# Create the main window
root = tk.Tk()
root.title("Magic Item Shop")

generate_button = tk.Button(root, text="Generate Magic Item", command=stock_shop_shelf)
generate_button.pack()
generate_button.pack(pady=10)

output_text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=40)
output_text_widget.pack()

# Start the GUI event loop
root.mainloop()
