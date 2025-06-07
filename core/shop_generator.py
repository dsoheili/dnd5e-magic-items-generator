"""
Core logic for generating shop inventories.
"""

import random
from common.common_methods import *
from common.magic_item_properties import *
from config.config import *


class ShopGenerator:
    """Handles generation of shop inventories."""
    
    def __init__(self):
        self.magic_items_url_data = get_magic_items_from_file("data/magic_items_data.txt")
        self.spells_url_data = get_magic_items_from_file("data/spells/spell_data.txt")
        
    def stock_magic_items_shop(self):
        """Generate magic items shop inventory."""
        items_without_url = []
        urls = []
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
            magic_item_url = get_item_url(magic_item_name, self.magic_items_url_data)
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
                
            if magic_item_url and magic_item_url.strip():  # Only add non-empty URLs
                output_text += f"<{magic_item_url}>\n"
                urls.append(magic_item_url)
            else:
                items_without_url.append(magic_item_name)
                
            output_text += "\n"
            
        output_text += "\n"
        for magic_item in items_without_url:
            output_text += f"!item {magic_item}\n"
            
        return {
            'output_text': output_text,
            'urls': urls
        }
        
    def stock_scroll_shop(self):
        """Generate spell scrolls shop inventory."""
        items_without_url = []
        urls = []
        output_text = ""
        
        for i in range(number_of_scroll_shop_items):
            spell_level = pick_random_rarity(scroll_rarities_probabilities)
            
            spell_level_text = get_xlation(spell_level)
            emoticons = get_emoticons(spell_level)
            spell_name = get_magic_spell(spell_level)
            item_price = get_item_price(spell_level)
            spell_url = get_item_url(spell_name, self.spells_url_data)
            
            output_text += f"**{spell_level_text}**\n"
            output_text += f"{emoticons}\n"
            output_text += f"Spell: *{spell_name}*\n"
            output_text += f"Price: {item_price:,} GP\n"
            
            if spell_url and spell_url.strip():  # Only add non-empty URLs
                output_text += f"<{spell_url}>\n"
                urls.append(spell_url)
            else:
                items_without_url.append(spell_name)
                
            output_text += "\n"
            
        output_text += "\n"
        for spell_scroll in items_without_url:
            output_text += f"!item {spell_scroll}\n"
            
        return {
            'output_text': output_text,
            'urls': urls
        }
        
    def stock_potion_shop(self):
        """Generate potions shop inventory."""
        items_without_url = []
        urls = []
        output_text = ""
        
        for i in range(number_of_potion_shop_items):
            potion_rarity = pick_random_rarity(potion_rarities_probabilities)
            
            potion_rarity_text = get_xlation(potion_rarity)
            emoticons = get_emoticons(potion_rarity)
            potion = get_potion(potion_rarity)
            item_price = get_item_price(potion_rarity)
            notes = generate_item_notes(potion)
            potion_url = get_item_url(potion, self.magic_items_url_data)
            
            output_text += f"**{potion}**\n"
            output_text += f"{emoticons}\n"
            output_text += f"*{potion_rarity_text}*\n"
            output_text += f"Price: {item_price:,} GP\n"
            
            if notes != "":
                output_text += f"{notes}\n"
                
            if potion_url and potion_url.strip():  # Only add non-empty URLs
                output_text += f"<{potion_url}>\n"
                urls.append(potion_url)
            else:
                items_without_url.append(potion)
                
            output_text += "\n"
            
        output_text += "\n"
        for potion in items_without_url:
            output_text += f"!item {potion}\n"
            
        return {
            'output_text': output_text,
            'urls': urls
        }
        
    def stock_basic_shop(self):
        """Generate basic items shop inventory."""
        items_without_url = []
        urls = []
        output_text = ""
        rarity = "basic"
        
        for i in range(number_of_basic_shop_items):
            item = get_magic_item(rarity)
            item_url = get_item_url(item, self.magic_items_url_data)
            
            # Simple mode
            output_text += f"- {item} - "
            
            if item_url and item_url.strip():  # Only add non-empty URLs
                output_text += f"<{item_url}>\n"
                urls.append(item_url)
            else:
                items_without_url.append(item)
                output_text += "\n"
                
        output_text += "\n"
        for item in items_without_url:
            output_text += f"!item {item}\n"
            
        return {
            'output_text': output_text,
            'urls': urls
        }
        
    def stock_combined_shop(self):
        """Generate combined shop inventory."""
        items_without_url = []
        urls = []
        output_text = ""
        
        for i in range(number_of_combined_shop_items):
            item = pick_random_rarity(combined_shop_rarities_probabilities)
            
            text = get_xlation(item)
            emoticons = get_emoticons(item)
            price = get_item_price(item)
            notes = ""
            
            price_text = f"{price:,} GP"
            
            # magic items handling
            if item in magic_items_rarities_probabilities:
                item_name = get_magic_item(item)
                notes = generate_item_notes(item_name)
                url = get_item_url(item_name, self.magic_items_url_data)
                
            # spell scroll handling
            elif item in scroll_rarities_probabilities:
                item_name = get_magic_spell(item)
                url = get_item_url(item_name, self.spells_url_data)
                
            # potion handling
            elif item in potion_rarities_probabilities:
                item_name = get_potion(item)
                notes = generate_item_notes(item_name)
                url = get_item_url(item_name, self.magic_items_url_data)
                
            # basic items handling
            else:
                item_name = get_magic_item(item)
                url = get_item_url(item_name, self.magic_items_url_data)
                price_text = "*Price on URL*"
                
            output_text += f"__**{item_name}**__\n"
            output_text += f"*{text}*\n"
            output_text += f"{emoticons}\n"
            output_text += f":moneybag: {price_text}\n"
            
            if notes != "":
                output_text += f"{notes}\n"
                
            if url and url.strip():  # Only add non-empty URLs
                output_text += f":mag_right: <{url}>\n"
                urls.append(url)
            else:
                items_without_url.append(item_name)
                
            output_text += "\n"
            
        output_text += "\n"
        for item in items_without_url:
            output_text += f"!item {item}\n"
            
        return {
            'output_text': output_text,
            'urls': urls
        }
