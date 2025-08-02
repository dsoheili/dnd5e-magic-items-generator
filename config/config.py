# Player character names for GUI
character_names = [
    "Gepeu",
    "Gnilbert",
    "Sally",
    "Zokira",
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
number_of_scroll_shop_items = 4
scroll_rarities_probabilities = {
    "level_0": 0.00,
    "level_1": 0.60,
    "level_2": 0.25,
    "level_3": 0.10,
    "level_4": 0.03,
    "level_5": 0.02,
    "level_6": 0.00,
    "level_7": 0.00,
    "level_8": 0.00,
    "level_9": 0.00
}

# ----- Potion Shop --------
number_of_potion_shop_items = 4
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
number_of_combined_shop_items = 10
combined_shop_rarities_probabilities = {
    "basic"             : 0.0,
    "common"            : 0.25,
    "uncommon_minor"    : 0.20,
    "rare_minor"        : 0,
    "very_rare_minor"   : 0,
    "legendary_minor"   : 0,
    "uncommon_major"    : 0.20,
    "rare_major"        : 0,
    "very_rare_major"   : 0,
    "legendary_major"   : 0,
    "mythic"            : 0,
    "unknown"           : 0,
    "level_0"           : 0.0,
    "level_1"           : 0.15,
    "level_2"           : 0.10,
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
    "beneficial_potion" : 0.05,
    "detrimental_potion": 0.05
}

price_ranges = {
    "basic"             : (50, 100),
    "common"            : (100, 200),
    "uncommon_minor"    : (320, 480),
    "rare_minor"        : (3200, 4800),
    "very_rare_minor"   : (32000, 48000),
    "legendary_minor"   : (160000, 240000),
    "uncommon_major"    : (400, 600),
    "rare_major"        : (4000, 6000),
    "very_rare_major"   : (40000, 60000),
    "legendary_major"   : (200000, 300000),
    "mythic"            : (250000, 400000),
    "unknown"           : (500000, 1000000),
    "level_0"           : (50, 50),
    "level_1"           : (100, 100),
    "level_2"           : (200, 200),
    "level_3"           : (400, 400),
    "level_4"           : (800, 800),
    "level_5"           : (1600, 1600),
    "level_6"           : (3200, 3200),
    "level_7"           : (6400, 6400),
    "level_8"           : (12800, 12800),
    "level_9"           : (25600, 25600),
    "common_potion"     : (50, 50),
    "uncommon_potion"   : (200, 200),
    "rare_potion"       : (2000, 2000),
    "very_rare_potion"  : (20000, 20000),
    "legendary_potion"  : (100000, 100000),
    "beneficial_potion" : (400, 900),
    "detrimental_potion": (400, 900)
}

# Simple gold drop ranges: CR -> (min_gold, max_gold) per monster
gold_drop_by_cr = {
    0:     (1, 5),        # avg 3 gp
    0.125: (2, 8),        # avg 5 gp
    0.25:  (3, 10),       # avg 6.5 gp
    0.5:   (5, 15),       # avg 10 gp
    1:     (10, 30),      # avg 20 gp
    2:     (25, 75),      # avg 50 gp
    3:     (40, 120),     # avg 80 gp
    4:     (75, 200),     # avg 137 gp
    5:     (100, 300),    # avg 200 gp
    6:     (150, 450),    # avg 300 gp
    7:     (200, 600),    # avg 400 gp
    8:     (300, 800),    # avg 550 gp
    9:     (400, 1000),   # avg 700 gp
    10:    (500, 1500),   # avg 1000 gp
    11:    (750, 2000),   # avg 1375 gp
    12:    (1000, 2500),  # avg 1750 gp
    13:    (1250, 3000),  # avg 2125 gp
    14:    (1500, 3500),  # avg 2500 gp
    15:    (2000, 4000),  # avg 3000 gp
    16:    (2500, 5000),  # avg 3750 gp
    17:    (3000, 6000),  # avg 4500 gp
    18:    (4000, 8000),  # avg 6000 gp
    19:    (5000, 10000), # avg 7500 gp
    20:    (6000, 12000), # avg 9000 gp
    21:    (8000, 15000), # avg 11500 gp
    22:    (10000, 18000),# avg 14000 gp
    23:    (12000, 20000),# avg 16000 gp
    24:    (15000, 25000),# avg 20000 gp
    25:    (18000, 30000),# avg 24000 gp
    30:    (25000, 50000),# avg 37500 gp
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
    "beneficial_potion" : ":champagne:",
    "detrimental_potion": ":test_tube:"
}

gui_info_text = """
| Tab | Dice            | Rarity           |
|-----|-----------------|------------------|
| A   | 3d100           | Common           |
| B   | 4d100           | Uncommon, minor  |
| C   | 3d100           | Rare, minor      |
| D   | 1d100+2d20      | Very Rare, minor |
| E   | 1d100           | Legendary, minor |
| F   | 2d100+3d20      | Uncommon, major  |
| G   | 5d100           | Rare, major      |
| H   | 3d100+1d20      | Very Rare, major |
| I   | 2d100+2d20      | Legendary, major |
| J   | 1d100           | Mythic           |
| K   | 1d20            | Unknown          |
| Z   | 4d100+1d20+1d10 | Basic            |
"""