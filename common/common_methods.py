import random
import csv
from common.magic_item_properties import *
from config.config import *


def get_item_price(rarity):
    min_price, max_price = price_ranges.get(rarity, (0, 0))
    return random.randint(min_price, max_price)


def roll_dice(max_value):
    return random.randint(1, max_value)


def get_magic_items_from_file(file_name):
    magic_items = []
    with open(file_name, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            magic_items.append(row)
    return magic_items

def get_magic_spell(spell_level):
    filename = f"data/spells/{spell_level}.csv"

    try:
        with open(filename, "r") as file:
            spells = [line.strip() for line in file.readlines() if line.strip()]

        if not spells:
            return None

        spell = random.choice(spells)
        return spell
    except FileNotFoundError:
        return None

def get_magic_item(rarity):
    filename = f"data/{rarity}.csv"

    try:
        with open(filename, "r") as file:
            items = [line.strip() for line in file.readlines() if line.strip()]

        if not items:
            return None

        item = random.choice(items)
        return item
    except FileNotFoundError:
        return None


def get_magic_item_url(magic_item_name, magic_items_info):
    for item_info in magic_items_info:
        if item_info[0] == magic_item_name:
            return item_info[1]
    return ""


def get_magic_item_from_table(table_number, row_number):
    if table_number not in table_mapping:
        print("Invalid table number.")
        return

    table_name = table_mapping[table_number]
    filename = f"data/{table_name}.csv"

    try:
        with open(filename, "r") as file:
            items = [line.strip() for line in file.readlines() if line.strip()]

        if not items:
            return None

        item = items[row_number - 1]  # Adjust row number to 0-based index
        return item
    except FileNotFoundError:
        return None


def determine_enchantment():
    enchantment_roll = random.random()
    enchantment_index = random.randint(0, 99)

    if enchantment_roll < curse_probability:
        return "Cursed", item_curses[enchantment_index]
    elif enchantment_roll < curse_probability + blessing_probability:
        return "Blessed", item_boons[enchantment_index]
    else:
        return None, None


def pick_random_rarity(probabilities):
    rand_val = random.random()
    cumulative_prob = 0

    for rarity, probability in probabilities.items():
        cumulative_prob += probability
        if rand_val <= cumulative_prob:
            return rarity

    # return first item as default
    return list(probabilities)[0]


def generate_item_notes(magic_item_name):
    notes = ""

    if "spell scroll" in magic_item_name.lower():
        spell_level = magic_item_name.split("(")[-1].replace(")", "").strip()
        if spell_level in spells_by_level:
            random_spell = random.choice(spells_by_level[spell_level])
            notes = "Spell: " + random_spell

    elif "of resistance" in magic_item_name.lower():
        notes = "Resistance: " + random.choice(resistance_types)

    return notes

def get_xlation(key):
    if key in xlations:
        return xlations[key]
    return key

def get_emoticons(key):
    if key in emoticons:
        return emoticons[key]
    return ""