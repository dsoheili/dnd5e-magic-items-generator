"""
Core logic for gold and price calculations.
"""

import random
from config.config import gold_drop_by_cr, price_ranges, item_condition_mapping
from common.common_methods import get_item_price


class GoldCalculator:
    """Handles gold drop calculations based on CR."""
    
    def calculate_drop(self, cr, num_monsters):
        """
        Calculate total gold drop for monsters.
        
        Args:
            cr: Challenge rating
            num_monsters: Number of monsters
            
        Returns:
            Total gold dropped
        """
        total_gp = 0
        
        # Find the appropriate range for this CR
        min_gold, max_gold = self.get_gold_range_for_cr(cr)
        
        for _ in range(num_monsters):
            gp_drop = random.randint(min_gold, max_gold)
            total_gp += gp_drop
            
        return total_gp
        
    def get_gold_range_for_cr(self, cr):
        """Get gold range for a specific CR, with fallback logic."""
        # Direct match first
        if cr in gold_drop_by_cr:
            return gold_drop_by_cr[cr]
            
        # Find closest CR if exact match not found
        available_crs = sorted(gold_drop_by_cr.keys())
        
        if cr < available_crs[0]:
            return gold_drop_by_cr[available_crs[0]]
        elif cr > available_crs[-1]:
            return gold_drop_by_cr[available_crs[-1]]
        else:
            # Find the closest CR
            closest_cr = min(available_crs, key=lambda x: abs(x - cr))
            return gold_drop_by_cr[closest_cr]


class PriceCalculator:
    """Handles item price calculations based on rarity and condition."""
    
    def calculate_price(self, rarity, condition):
        """
        Calculate item price based on rarity and condition.
        
        Args:
            rarity: Item rarity key
            condition: Item condition key
            
        Returns:
            Tuple of (base_price, adjusted_price)
        """
        base_price = get_item_price(rarity)
        condition_modifier = item_condition_mapping.get(condition, 1.0)
        adjusted_price = int(base_price * condition_modifier)
        
        return base_price, adjusted_price
