# Player character names for GUI
character_names = [
    "Anya",
    "Faewynn",
    "Josephine",
    "Nex",
    "Silvanus",
    "Thalia",
    "Wabuu",
    "NPC"
]

# ----- Enchantments ------------
# Determines if magic item shop applies curses/boons to items
magic_item_enchantments_enabled = False
curse_probability               = 0.65
blessing_probability            = 0.05
# ---------------------------


# ----- Magic Items Shop --------
# Number of items available in the magic item shop
number_of_magic_items_shop_items = 12

default_magic_items_shop_rarity = "common"
magic_items_shop_predefined_rarities = [
    ["common"],
    ["common"],
    ["uncommon_minor","uncommon_major"],
    ["uncommon_minor","uncommon_major"],
    ["rare_minor","rare_major"],
    ["very_rare_minor","very_rare_major"],
    ["legendary_minor","legendary_major"],
]

# For rolling stock of magic item shop
random_rarities_for_magic_items_shop = True

magic_items_rarities_probabilities = {
    "common"         : 0.20,
    "uncommon_minor" : 0.15,
    "rare_minor"     : 0.10,
    "very_rare_minor": 0.10,
    "legendary_minor": 0.05,
    "uncommon_major" : 0.15,
    "rare_major"     : 0.10,
    "very_rare_major": 0.10,
    "legendary_major": 0.05,
    "mythic"         : 0,
    "unknown"        : 0
}

magic_items_rarity_ranges = {
    (1, 20)   : 1, # common
    (21, 40)  : 2, # uncommon_minor
    (41, 55)  : 6, # uncommon_major
    (56, 70)  : 3, # rare_minor
    (71, 80)  : 7, # rare_major
    (81, 90)  : 4, # very_rare_minor
    (91, 95)  : 8, # very_rare_major
    (96, 97)  : 5, # legendary_minor
    (98, 99)  : 9, # legendary_major
    (100, 100): 10 # mythic
}


# ----- Spell Scrolls Shop --------
number_of_scroll_shop_items = 8
scroll_rarities_probabilities = {
    "level_0": 0.00,
    "level_1": 0.10,
    "level_2": 0.15,
    "level_3": 0.15,
    "level_4": 0.15,
    "level_5": 0.15,
    "level_6": 0.10,
    "level_7": 0.10,
    "level_8": 0.05,
    "level_9": 0.05
}

# ----- Potion Shop --------
number_of_potion_shop_items = 8
potion_rarities_probabilities = {
    "common_potion"     : 0,
    "uncommon_potion"   : 0,
    "rare_potion"       : 0,
    "very_rare_potion"  : 0,
    "legendary_potion"  : 0,
    "beneficial_potion" : 0.50,
    "detrimental_potion": 0.50
}

# ----- Basic Shop --------
number_of_basic_shop_items = 10

item_condition_mapping = {
    "mint"        : 1.00, # Item is in perfect condition
    "lightly_used": 0.80, # Item has minimal signs of wear
    "used"        : 0.65, # Item shows noticeable wear
    "heavily_used": 0.50, # Item is functional but shows significant wear
    "damaged"     : 0.25, # Item needs repair to be fully functional
    "broken"      : 0.10  # Item is non-functional, requires major repairs
}

# ----- Combined Shop --------
number_of_combined_shop_items = 12
combined_shop_rarities_probabilities = {
    "basic"             : 0,
    "common"            : 0,
    "uncommon_minor"    : 0.10,
    "rare_minor"        : 0.25,
    "very_rare_minor"   : 0.10,
    "legendary_minor"   : 0.10,
    "uncommon_major"    : 0.10,
    "rare_major"        : 0.15,
    "very_rare_major"   : 0.10,
    "legendary_major"   : 0.10,
    "mythic"            : 0,
    "unknown"           : 0,
    "level_0"           : 0,
    "level_1"           : 0,
    "level_2"           : 0,
    "level_3"           : 0,
    "level_4"           : 0,
    "level_5"           : 0,
    "level_6"           : 0,
    "level_7"           : 0,
    "level_8"           : 0,
    "level_9"           : 0,
    "common_potion"     : 0,
    "uncommon_potion"   : 0,
    "rare_potion"       : 0,
    "very_rare_potion"  : 0,
    "legendary_potion"  : 0,
    "beneficial_potion" : 0,
    "detrimental_potion": 0
}

price_ranges = {
    "basic"             : (50, 300),
    "common"            : (300, 500),
    "uncommon_minor"    : (501, 1000),
    "rare_minor"        : (1001, 5000),
    "very_rare_minor"   : (5001, 10000),
    "legendary_minor"   : (10001, 20000),
    "uncommon_major"    : (1000, 2000),
    "rare_major"        : (5001, 10000),
    "very_rare_major"   : (10001, 25000),
    "legendary_major"   : (25001, 50000),
    "mythic"            : (50001, 100000),
    "unknown"           : (100000, 200000),
    "level_0"           : (10, 50),
    "level_1"           : (200, 400),
    "level_2"           : (400, 800),
    "level_3"           : (1000, 2000),
    "level_4"           : (2000, 4000),
    "level_5"           : (4000, 10000),
    "level_6"           : (10000, 15000),
    "level_7"           : (15000, 25000),
    "level_8"           : (25000, 30000),
    "level_9"           : (30000, 40000),
    "common_potion"     : (100, 500),
    "uncommon_potion"   : (501, 1000),
    "rare_potion"       : (1001, 5000),
    "very_rare_potion"  : (5001, 10000),
    "legendary_potion"  : (10001, 20000),
    "beneficial_potion" : (600, 1200),
    "detrimental_potion": (700, 1500)
}

xlations = {
    "basic"             : "Basic",
    "common"            : "Common",
    "uncommon_minor"    : "Uncommon, Minor",
    "rare_minor"        : "Rare, Minor",
    "very_rare_minor"   : "Very Rare, Minor",
    "legendary_minor"   : "Legendary, Minor",
    "uncommon_major"    : "Uncommon, Major",
    "rare_major"        : "Rare, Major",
    "very_rare_major"   : "Very Rare, Major",
    "legendary_major"   : "Legendary, Major",
    "mythic"            : "Mythic",
    "unknown"           : "Unknown",
    "level_0"           : "Spell Scroll (Cantrip)",
    "level_1"           : "Spell Scroll (1st Level)",
    "level_2"           : "Spell Scroll (2nd Level)",
    "level_3"           : "Spell Scroll (3rd Level)",
    "level_4"           : "Spell Scroll (4th Level)",
    "level_5"           : "Spell Scroll (5th Level)",
    "level_6"           : "Spell Scroll (6th Level)",
    "level_7"           : "Spell Scroll (7th Level)",
    "level_8"           : "Spell Scroll (8th Level)",
    "level_9"           : "Spell Scroll (9th Level)",
    "common_potion"     : "Common",
    "uncommon_potion"   : "Uncommon",
    "rare_potion"       : "Rare",
    "very_rare_potion"  : "Very Rare",
    "legendary_potion"  : "Legendary",
    "beneficial_potion" : "Beneficial Mixture",
    "detrimental_potion": "Detrimental Mixture",
    "mint"              : "Mint",
    "lightly_used"      : "Lightly Used",
    "used"              : "Used",
    "heavily_used"      : "Heavily Used",
    "damaged"           : "Damaged",
    "broken"            : "Broken"
}

emoticons = {
    "basic"             : ":sparkles:",
    "common"            : ":star:",
    "uncommon_minor"    : ":star::star:",
    "rare_minor"        : ":star::star::star:",
    "very_rare_minor"   : ":star::star::star::star:",
    "legendary_minor"   : ":star::star::star::star::star:",
    "uncommon_major"    : ":star2::star2:",
    "rare_major"        : ":star2::star2::star2:",
    "very_rare_major"   : ":star2::star2::star2::star2:",
    "legendary_major"   : ":star2::star2::star2::star2::star2:",
    "mythic"            : ":sunny:",
    "unknown"           : ":new_moon:",
    "level_0"           : ":roll_of_paper:",
    "level_1"           : ":scroll:",
    "level_2"           : ":scroll::scroll:",
    "level_3"           : ":scroll::scroll::scroll:",
    "level_4"           : ":scroll::scroll::scroll::scroll:",
    "level_5"           : ":scroll::scroll::scroll::scroll::scroll:",
    "level_6"           : ":scroll::scroll::scroll::scroll::scroll::scroll:",
    "level_7"           : ":scroll::scroll::scroll::scroll::scroll::scroll::scroll:",
    "level_8"           : ":scroll::scroll::scroll::scroll::scroll::scroll::scroll::scroll:",
    "level_9"           : ":scroll::scroll::scroll::scroll::scroll::scroll::scroll::scroll::scroll:",
    "common_potion"     : ":alembic:",
    "uncommon_potion"   : ":alembic::alembic:",
    "rare_potion"       : ":alembic::alembic::alembic:",
    "very_rare_potion"  : ":alembic::alembic::alembic::alembic:",
    "legendary_potion"  : ":alembic::alembic::alembic::alembic::alembic:",
    "beneficial_potion" : ":champagne::champagne::champagne:",
    "detrimental_potion": ":test_tube::test_tube::test_tube:"
}

gui_info_text = """
| 1d100 | Table  | Dice            | Max | Rarity           |
|-------|--------|-----------------|-----|------------------|
| 1-20  | 1  - A | 3d100           | 200 | Common           |
| 21-40 | 2  - B | 4d100           | 400 | Uncommon, minor  |
| 56-70 | 3  - C | 3d100           | 300 | Rare, minor      |
| 81-90 | 4  - D | 1d100+2d20      | 140 | Very Rare, minor |
| 96-97 | 5  - E | 1d100           | 100 | Legendary, minor |
| 41-55 | 6  - F | 2d100+3d20      | 260 | Uncommon, major  |
| 71-80 | 7  - G | 4d100           | 400 | Rare, major      |
| 91-95 | 8  - H | 3d100           | 300 | Very Rare, major |
| 98-99 | 9  - I | 2d100           | 200 | Legendary, major |
| 100   | 10 - J | 1d100           | 100 | Mythic           |
| N/A   | 11 - K | 1d12            | 12  | Unknown          |
| 0     | 0  - Z | 4d100+1d20+1d10 | 430 | Basic            |
"""