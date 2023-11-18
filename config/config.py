# Player character names for GUI
character_names = [
    "Hopper",
    "Olo",
    "Skellor",
    "Urashi",
    "Winnera",
    "NPC"
]

# ----- Enchantments --------
# Determines if magic item shop applies curses/boons to items
magic_item_enchantments_enabled = True
curse_probability = 0.65
blessing_probability = 0.05
# ---------------------------

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
    "unknown": (200000,300000)
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
    "unknown": "Unknown"
}

gui_info_text = """
| Table  | Dice           | Max | Rarity           |
|--------|----------------|-----|------------------|
| 1  - A | 1d100+1d20     | 120 | Common           |
| 2  - B | 1d100+3d20     | 160 | Uncommon, minor  |
| 3  - C | 1d100+2d20     | 140 | Rare, minor      |
| 4  - D | 1d100          | 100 | Very Rare, minor |
| 5  - E | 1d100          | 100 | Legendary, minor |
| 6  - F | 1d100+1d20     | 120 | Uncommon, major  |
| 7  - G | 2d100+1d20     | 220 | Rare, major      |
| 8  - H | 1d100+3d20     | 160 | Very Rare, major |
| 9  - I | 1d100+1d20+1d6 | 126 | Legendary, major |
| 10 - J | 2d20+1d12      | 52  | Mythic           |
| 11 - K | 1d12           | 12  | Unknown          |
"""