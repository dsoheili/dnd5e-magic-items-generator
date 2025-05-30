import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from common.magic_item_properties import *
from common.common_methods import *
from config.config import *

magic_items_url_data = get_magic_items_from_file("data/magic_items_data.txt")
spells_url_data = get_magic_items_from_file("data/spells/spell_data.txt")

def stock_magic_items_shop_shelf():
    items_without_url = []
    output_text = ""

    for i in range(number_of_magic_items_shop_items):
        if random_rarities_for_magic_items_shop:
            rarity = pick_random_rarity(magic_items_rarities_probabilities)
        else:
            if i < len(magic_items_shop_predefined_rarities):
                rarity = random.choice(magic_items_shop_predefined_rarities[i])
            else:
                rarity = default_magic_items_shop_rarity

        rarity_text = get_xlation(rarity)
        magic_item_name = get_magic_item(rarity)
        item_price = get_item_price(rarity)
        notes = generate_item_notes(magic_item_name)
        magic_item_url = get_item_url(magic_item_name, magic_items_url_data)
        emoticons = get_emoticons(rarity)

        enchanted = None
        if magic_item_enchantments_enabled:
            enchanted, enchantment_effect = determine_enchantment()

        output_text += f"**{magic_item_name}**\n"
        output_text += f"{emoticons}\n"
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

def stock_scroll_shop_shelf():
    items_without_url = []
    output_text = ""

    for i in range(number_of_scroll_shop_items):
        spell_level = pick_random_rarity(scroll_rarities_probabilities)

        spell_level_text = get_xlation(spell_level)
        emoticons = get_emoticons(spell_level)
        spell_name = get_magic_spell(spell_level)
        item_price = get_item_price(spell_level)
        spell_url = get_item_url(spell_name, spells_url_data)

        output_text += f"**{spell_level_text}**\n"
        output_text += f"{emoticons}\n"
        output_text += f"Spell: *{spell_name}*\n"
        output_text += f"Price: {item_price:,} GP\n"

        if spell_url:
            output_text += f"<{spell_url}>\n"
        else:
            items_without_url.append(spell_name)

        output_text += "\n"

    output_text += "\n"
    for spell_scroll in items_without_url:
        output_text += f"!item {spell_scroll}\n"

        output_text += "\n"

    output_text_widget.delete(1.0, tk.END)
    output_text_widget.insert(tk.END, output_text)

def stock_potion_shop_shelf():
    items_without_url = []
    output_text = ""

    for i in range(number_of_potion_shop_items):
        potion_rarity = pick_random_rarity(potion_rarities_probabilities)

        potion_rarity_text = get_xlation(potion_rarity)
        emoticons = get_emoticons(potion_rarity)
        potion = get_potion(potion_rarity)
        item_price = get_item_price(potion_rarity)
        notes = generate_item_notes(potion)
        potion_url = get_item_url(potion, magic_items_url_data)

        output_text += f"**{potion}**\n"
        output_text += f"{emoticons}\n"
        output_text += f"*{potion_rarity_text}*\n"
        output_text += f"Price: {item_price:,} GP\n"

        if notes != "":
            output_text += f"{notes}\n"

        if potion_url:
            output_text += f"<{potion_url}>\n"
        else:
            items_without_url.append(potion)

        output_text += "\n"

    output_text += "\n"
    for potion in items_without_url:
        output_text += f"!item {potion}\n"

    output_text_widget.delete(1.0, tk.END)
    output_text_widget.insert(tk.END, output_text)

def stock_basic_shop_shelf():
    items_without_url = []
    output_text = ""
    rarity = "basic"
    # rarity_text = get_xlation(rarity)
    # emoticon = get_emoticons(rarity)

    for i in range(number_of_basic_shop_items):
        item = get_magic_item(rarity)
        item_url = get_item_url(item, magic_items_url_data)

        # output_text += f"**{item}**\n"
        # output_text += f"{emoticon}\n"
        # output_text += f"*{rarity_text}*\n"

        # Simple mode
        output_text += f"- {item} - "

        if item_url:
            output_text += f"<{item_url}>\n"
        else:
            items_without_url.append(item)

        # output_text += "\n"

    output_text += "\n"
    for item in items_without_url:
        output_text += f"!item {item}\n"

    output_text_widget.delete(1.0, tk.END)
    output_text_widget.insert(tk.END, output_text)

def stock_combined_shop_shelf():
    items_without_url = []
    output_text = ""

    for i in range(number_of_combined_shop_items):
        item = pick_random_rarity(combined_shop_rarities_probabilities)

        text = get_xlation(item)
        emoticons = get_emoticons(item)
        price = get_item_price(item)
        notes = ""

        price = f"{price:,} GP"

        # magic items handling
        if item in magic_items_rarities_probabilities:
            item_name = get_magic_item(item)
            notes = generate_item_notes(item_name)
            url = get_item_url(item_name, magic_items_url_data)

        # spell scroll handling
        elif item in scroll_rarities_probabilities:
            item_name = get_magic_spell(item)
            url = get_item_url(item_name, spells_url_data)

        # potion handling
        elif item in potion_rarities_probabilities:
            item_name = get_potion(item)
            notes = generate_item_notes(item_name)
            url = get_item_url(item_name, magic_items_url_data)

        # basic items handling
        else:
            item_name = get_magic_item(item)
            url = get_item_url(item_name, magic_items_url_data)
            price = "*Price on URL*"


        output_text += f"__**{item_name}**__\n"
        output_text += f"*{text}*\n"
        output_text += f"{emoticons}\n"
        output_text += f":moneybag: {price}\n"

        if notes != "":
            output_text += f"{notes}\n"

        if url:
            output_text += f":mag_right: <{url}>\n"
        else:
            items_without_url.append(item_name)

        output_text += "\n"

    output_text += "\n"
    for item in items_without_url:
        output_text += f"!item {item}\n"

    output_text_widget.delete(1.0, tk.END)
    output_text_widget.insert(tk.END, output_text)

# Create the main window
root = tk.Tk()
root.title("Magic Item Shop")
root.geometry("800x600")  # Set the size of the window

# Create a frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

# Improve button appearance and organization
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 10), padding=8)

generate_button = ttk.Button(button_frame, text="Generate Magic Items", command=stock_magic_items_shop_shelf)
generate_button.pack(side=tk.LEFT, padx=6)

generate_scrolls_button = ttk.Button(button_frame, text="Generate Spell Scrolls", command=stock_scroll_shop_shelf)
generate_scrolls_button.pack(side=tk.LEFT, padx=6)

generate_potions_button = ttk.Button(button_frame, text="Generate Potions", command=stock_potion_shop_shelf)
generate_potions_button.pack(side=tk.LEFT, padx=6)

generate_basic_button = ttk.Button(button_frame, text="Generate Basic Items", command=stock_basic_shop_shelf)
generate_basic_button.pack(side=tk.LEFT, padx=6)

generate_basic_button = ttk.Button(button_frame, text="Generate Combined", command=stock_combined_shop_shelf)
generate_basic_button.pack(side=tk.LEFT, padx=6)

# Create a scrolled text widget for output
output_text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=('Helvetica', 11))
output_text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Start the GUI event loop
root.mainloop()
