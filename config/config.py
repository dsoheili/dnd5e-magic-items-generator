# Player character names for GUI
character_names = [
    "Anweira",
    "Elara",
    "Hopper",
    "Olo",
    "Skellor",
    "Urashi",
    "NPC"
]

# ----- Enchantments ------------
# Determines if magic item shop applies curses/boons to items
magic_item_enchantments_enabled = True
curse_probability = 0.65
blessing_probability = 0.05
# ---------------------------


# ----- Magic Items Shop --------
# Number of items available in the magic item shop
number_of_shop_items = 7

default_shop_rarity = "common"
shop_items_predefined_rarities = [
    ["common"],
    ["common"],
    ["uncommon_minor","uncommon_major"],
    ["uncommon_minor","uncommon_major"],
    ["rare_minor","rare_major"],
    ["very_rare_minor","very_rare_major"],
    ["legendary_minor","legendary_major"],
]

# For rolling stock of magic item shop
random_rarities_for_shop_items = False
rarities_probabilities = {
    "common": 0.3,
    "uncommon_minor": 0.1,
    "rare_minor": 0.1,
    "very_rare_minor": 0.1,
    "legendary_minor": 0.05,
    "uncommon_major": 0.1,
    "rare_major": 0.05,
    "very_rare_major": 0.05,
    "legendary_major": 0.05,
    "mythic": 0,
    "unknown": 0
}

price_ranges = {
    "common": (10, 50),
    "uncommon_minor": (50, 250),
    "rare_minor": (500, 5000),
    "very_rare_minor": (5000, 10000),
    "legendary_minor": (10000, 50000),
    "uncommon_major": (50, 300),
    "rare_major": (1000, 10000),
    "very_rare_major": (10000, 25000),
    "legendary_major": (25000, 50000),
    "mythic": (100000,200000),
    "unknown": (200000,300000),
    "level_0": (50, 100),
    "level_1": (100, 300),
    "level_2": (300, 500),
    "level_3": (500, 800),
    "level_4": (800, 1200),
    "level_5": (1200, 2500),
    "level_6": (2500, 5500),
    "level_7": (5500, 8000),
    "level_8": (8000, 12000),
    "level_9": (12000, 16000),
    "common_potion": (50, 250),
    "uncommon_potion": (250, 400),
    "rare_potion": (750, 1000),
    "very_rare_potion": (1500, 2000),
    "legendary_potion": (8500, 10000)
}

xlations = {
    "common": "Common",
    "uncommon_minor": "Uncommon, Minor",
    "rare_minor": "Rare, Minor",
    "very_rare_minor": "Very Rare, Minor",
    "legendary_minor": "Legendary, Minor",
    "uncommon_major": "Uncommon, Major",
    "rare_major": "Rare, Major",
    "very_rare_major": "Very Rare, Major",
    "legendary_major": "Legendary, Major",
    "mythic": "Mythic",
    "unknown": "Unknown",
    "level_0": "Spell Scroll (Cantrip)",
    "level_1": "Spell Scroll (1st Level)",
    "level_2": "Spell Scroll (2nd Level)",
    "level_3": "Spell Scroll (3rd Level)",
    "level_4": "Spell Scroll (4th Level)",
    "level_5": "Spell Scroll (5th Level)",
    "level_6": "Spell Scroll (6th Level)",
    "level_7": "Spell Scroll (7th Level)",
    "level_8": "Spell Scroll (8th Level)",
    "level_9": "Spell Scroll (9th Level)",
    "common_potion": "Common",
    "uncommon_potion": "Uncommon",
    "rare_potion": "Rare",
    "very_rare_potion": "Very Rare",
    "legendary_potion": "Legendary"
}

emoticons = {
    "common": ":star:",
    "uncommon_minor": ":star::star:",
    "rare_minor": ":star::star::star:",
    "very_rare_minor": ":star::star::star::star:",
    "legendary_minor": ":star::star::star::star::star:",
    "uncommon_major": ":star2::star2:",
    "rare_major": ":star2::star2::star2:",
    "very_rare_major": ":star2::star2::star2::star2:",
    "legendary_major": ":star2::star2::star2::star2::star2:",
    "mythic": ":sunny:",
    "unknown": ":new_moon:",
    "level_0": ":dizzy:",
    "level_1": ":star:",
    "level_2": ":star::star:",
    "level_3": ":star::star::star:",
    "level_4": ":star::star::star::star:",
    "level_5": ":star::star::star::star::star:",
    "level_6": ":star::star::star::star::star::star:",
    "level_7": ":star::star::star::star::star::star::star:",
    "level_8": ":star::star::star::star::star::star::star::star:",
    "level_9": ":star::star::star::star::star::star::star::star::star:",
    "common_potion": ":alembic:",
    "uncommon_potion": ":alembic::alembic:",
    "rare_potion": ":alembic::alembic::alembic:",
    "very_rare_potion": ":alembic::alembic::alembic::alembic:",
    "legendary_potion": ":alembic::alembic::alembic::alembic::alembic:"
}

gui_info_text = """
| Table  | Dice            | Max | Rarity           |
|--------|-----------------|-----|------------------|
| 1  - A | 1d100+1d20      | 120 | Common           |
| 2  - B | 1d100+3d20      | 160 | Uncommon, minor  |
| 3  - C | 1d100+2d20+1d6  | 146 | Rare, minor      |
| 4  - D | 1d100           | 100 | Very Rare, minor |
| 5  - E | 1d100           | 100 | Legendary, minor |
| 6  - F | 1d100+1d20      | 120 | Uncommon, major  |
| 7  - G | 2d100+1d20      | 220 | Rare, major      |
| 8  - H | 1d100+3d20      | 160 | Very Rare, major |
| 9  - I | 1d100+1d20+1d12 | 132 | Legendary, major |
| 10 - J | 2d20+4d4        | 56  | Mythic           |
| 11 - K | 1d12            | 12  | Unknown          |
"""


# ----- Spell Scrolls Shop --------
number_of_scroll_shop_items = 5
scroll_rarities_probabilities = {
    "level_0": 0.3,
    "level_1": 0.1,
    "level_2": 0.1,
    "level_3": 0.1,
    "level_4": 0.1,
    "level_5": 0.05,
    "level_6": 0.05,
    "level_7": 0.05,
    "level_8": 0.025,
    "level_9": 0.025
}

# ----- Potion Shop --------
number_of_potion_shop_items = 5
potion_rarities_probabilities = {
    "common_potion": 0.30,
    "uncommon_potion": 0.30,
    "rare_potion": 0.25,
    "very_rare_potion": 0.10,
    "legendary_potion": 0.05,
}