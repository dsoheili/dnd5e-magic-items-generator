"""
Core logic for generating magic items.
"""

import random
from common.common_methods import *
from common.magic_item_properties import *
from config.config import *


class ItemGenerator:
    """Handles generation of individual magic items."""
    
    def __init__(self):
        self.magic_items_info = get_magic_items_from_file("data/magic_items_data.txt")
        self.spells_info = get_magic_items_from_file("data/spells/spell_data.txt")
        self.table_d100_var = ""  # Compatibility with original code
        
    def generate_magic_item(self, character_name="Unknown", table_number=None, row_number=None):
        """
        Generate a magic item with specified parameters.
        
        Args:
            character_name: Name of the character finding the item
            table_number: Specific table number (1-11) or None for random
            row_number: Specific row number or None for random
            
        Returns:
            Dictionary with output_text and url
        """
        # Determine rarity
        if table_number is not None:
            rarity = table_mapping.get(table_number, table_mapping[0])
        elif self.table_d100_var != "":
            table_d100 = int(self.table_d100_var)
            rarity = determine_rarity_from_d100(table_d100)
        else:
            rarity = pick_random_rarity(magic_items_rarities_probabilities)
            
        # Get item
        if row_number is None:
            magic_item_name = get_magic_item(rarity)
        else:
            magic_item_name = get_magic_item_from_table(rarity, row_number)
            
        # Generate item details
        notes = generate_item_notes(magic_item_name)
        item_price = get_item_price(rarity)
        magic_item_url = get_item_url(magic_item_name, self.magic_items_info)
        rarity_text = get_xlation(rarity)
        emoticons = get_emoticons(rarity)
        
        # Build output text
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
            output_text += f"\n!item {magic_item_name}"
            
        return {
            'output_text': output_text,
            'url': magic_item_url
        }
        
    def generate_random_spell(self, spell_level):
        """
        Generate a random spell of the specified level.
        
        Args:
            spell_level: Spell level (0-9)
            
        Returns:
            Dictionary with output_text and url
        """
        # Map spell level to the file name format
        level_key = f"level_{spell_level}"
        
        # Get random spell
        spell_name = get_magic_spell(level_key)
        
        if not spell_name:
            output_text = f"No spells found for level {spell_level}"
            return {
                'output_text': output_text,
                'url': ''
            }
        
        # Get spell URL
        spell_url = get_item_url(spell_name, self.spells_info)
        
        # Get spell scroll price
        spell_price = get_item_price(level_key)
        
        # Format spell level text
        if spell_level == 0:
            level_text = "Cantrip"
        elif spell_level == 1:
            level_text = "1st Level"
        elif spell_level == 2:
            level_text = "2nd Level"
        elif spell_level == 3:
            level_text = "3rd Level"
        else:
            level_text = f"{spell_level}th Level"
        
        # Build output
        output_text = f"**Random Spell Scroll Generated**\n"
        output_text += f"```\n"
        output_text += f"Spell Name: {spell_name}\n"
        output_text += f"Spell Level: {level_text}\n"
        output_text += f"Scroll Value: {spell_price:,} gp\n"
        output_text += f"```\n"
        
        if spell_url and spell_url.strip():
            output_text += f"URL: <{spell_url}>\n"
        else:
            output_text += f"\n!spell {spell_name}"
            
        return {
            'output_text': output_text,
            'url': spell_url
        }