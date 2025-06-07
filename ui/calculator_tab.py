"""
Gold and Price Calculator tab UI.
"""

import tkinter as tk
from tkinter import ttk
from core.calculators import GoldCalculator, PriceCalculator
from config.config import price_ranges, item_condition_mapping


class CalculatorTab:
    """Tab for gold drop and item price calculations."""
    
    def __init__(self, parent):
        self.parent = parent
        self.gold_calc = GoldCalculator()
        self.price_calc = PriceCalculator()
        self.create_widgets()
        
    def create_widgets(self):
        """Create all widgets for the calculator tab."""
        # Main container with two columns
        main_frame = ttk.Frame(self.parent, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure custom styles
        self.setup_styles()
        
        # Create horizontal layout for calculators
        calc_container = ttk.Frame(main_frame)
        calc_container.pack(fill=tk.BOTH, expand=True)
        
        # Left column - Gold calculator
        left_frame = ttk.Frame(calc_container)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.create_gold_calculator(left_frame)
        
        # Right column - Price calculator
        right_frame = ttk.Frame(calc_container)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.create_price_calculator(right_frame)
        
    def setup_styles(self):
        """Configure custom styles for better appearance."""
        style = ttk.Style()
        
        # Configure custom colors
        style.configure('Calc.TLabelframe', background='#f0f0f0')
        style.configure('Calc.TLabelframe.Label', background='#f0f0f0', font=('Segoe UI', 10, 'bold'))
        
        # Calculator button styles
        style.configure('Calculate.TButton', font=('Segoe UI', 9, 'bold'))
        style.map('Calculate.TButton',
                  foreground=[('active', '#ffffff')],
                  background=[('active', '#0078d4')])
                  
    def create_gold_calculator(self, parent):
        """Create gold drop calculator section."""
        calc_frame = ttk.LabelFrame(parent, text="💰 Gold Drop Calculator", padding="15", style='Calc.TLabelframe')
        calc_frame.pack(fill=tk.BOTH, expand=True)
        
        # Description
        desc = ttk.Label(
            calc_frame,
            text="Calculate gold drops from defeated monsters",
            font=('Segoe UI', 9, 'italic'),
            foreground='#666666'
        )
        desc.pack(anchor=tk.W, pady=(0, 15))
        
        # Input frame
        input_frame = ttk.Frame(calc_frame)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        # CR input
        cr_label = ttk.Label(input_frame, text="Challenge Rating (CR):", font=('Segoe UI', 9))
        cr_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.cr_var = tk.StringVar()
        cr_entry = ttk.Entry(input_frame, textvariable=self.cr_var, width=15, font=('Segoe UI', 9))
        cr_entry.grid(row=0, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # CR help text
        cr_help = ttk.Label(
            input_frame,
            text="e.g., 0.5, 1, 5, 10",
            font=('Segoe UI', 8, 'italic'),
            foreground='#999999'
        )
        cr_help.grid(row=0, column=2, sticky=tk.W, padx=(10, 0))
        
        # Number of monsters
        monsters_label = ttk.Label(input_frame, text="Number of Monsters:", font=('Segoe UI', 9))
        monsters_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.num_monsters_var = tk.StringVar(value="1")
        monsters_entry = ttk.Entry(input_frame, textvariable=self.num_monsters_var, width=15, font=('Segoe UI', 9))
        monsters_entry.grid(row=1, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Separator
        separator1 = ttk.Separator(calc_frame, orient='horizontal')
        separator1.pack(fill=tk.X, pady=10)
        
        # Calculate button
        calc_btn = ttk.Button(
            calc_frame,
            text="🎲 Calculate Gold Drop",
            command=self.calculate_gold,
            style='Calculate.TButton'
        )
        calc_btn.pack(anchor=tk.W, pady=(0, 15))
        
        # Result display
        result_frame = ttk.LabelFrame(calc_frame, text="📊 Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.gold_result = tk.Text(
            result_frame,
            height=6,
            width=40,
            font=('Segoe UI', 11),
            wrap=tk.WORD,
            relief=tk.GROOVE,
            background='#ffffff',
            borderwidth=1
        )
        self.gold_result.pack(fill=tk.BOTH, expand=True)
        
        # Add example text
        self.gold_result.insert(tk.END, "Enter CR and number of monsters,\nthen click Calculate.")
        self.gold_result.configure(state='disabled')
        
    def create_price_calculator(self, parent):
        """Create item price calculator section."""
        calc_frame = ttk.LabelFrame(parent, text="💎 Item Price Calculator", padding="15", style='Calc.TLabelframe')
        calc_frame.pack(fill=tk.BOTH, expand=True)
        
        # Description
        desc = ttk.Label(
            calc_frame,
            text="Calculate item value based on rarity and condition",
            font=('Segoe UI', 9, 'italic'),
            foreground='#666666'
        )
        desc.pack(anchor=tk.W, pady=(0, 15))
        
        # Input frame
        input_frame = ttk.Frame(calc_frame)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Rarity selection
        rarity_label = ttk.Label(input_frame, text="Item Rarity:", font=('Segoe UI', 9))
        rarity_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.rarity_var = tk.StringVar()
        
        rarity_combo = ttk.Combobox(
            input_frame,
            textvariable=self.rarity_var,
            values=list(price_ranges.keys()),
            state="readonly",
            width=20,
            font=('Segoe UI', 9)
        )
        rarity_combo.grid(row=0, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Condition selection
        condition_label = ttk.Label(input_frame, text="Item Condition:", font=('Segoe UI', 9))
        condition_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.condition_var = tk.StringVar(value="mint")
        
        condition_combo = ttk.Combobox(
            input_frame,
            textvariable=self.condition_var,
            values=list(item_condition_mapping.keys()),
            state="readonly",
            width=20,
            font=('Segoe UI', 9)
        )
        condition_combo.grid(row=1, column=1, sticky=tk.W, pady=5, padx=(10, 0))
        
        # Separator
        separator2 = ttk.Separator(calc_frame, orient='horizontal')
        separator2.pack(fill=tk.X, pady=10)
        
        # Calculate button
        calc_btn = ttk.Button(
            calc_frame,
            text="💵 Calculate Item Price",
            command=self.calculate_price,
            style='Calculate.TButton'
        )
        calc_btn.pack(anchor=tk.W, pady=(0, 15))
        
        # Result display
        result_frame = ttk.LabelFrame(calc_frame, text="📊 Result", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True)
        
        self.price_result = tk.Text(
            result_frame,
            height=6,
            width=40,
            font=('Segoe UI', 11),
            wrap=tk.WORD,
            relief=tk.GROOVE,
            background='#ffffff',
            borderwidth=1
        )
        self.price_result.pack(fill=tk.BOTH, expand=True)
        
        # Add example text
        self.price_result.insert(tk.END, "Select rarity and condition,\nthen click Calculate.")
        self.price_result.configure(state='disabled')
        
    def calculate_gold(self):
        """Calculate gold drop based on CR and number of monsters."""
        try:
            cr = float(self.cr_var.get())
            num_monsters = int(self.num_monsters_var.get())
            
            total_gold = self.gold_calc.calculate_drop(cr, num_monsters)
            avg_per_monster = total_gold // num_monsters if num_monsters > 0 else 0
            
            self.gold_result.configure(state='normal')
            self.gold_result.delete("1.0", tk.END)
            self.gold_result.insert(
                tk.END,
                f"🏆 Calculation Results:\n\n"
                f"Total Gold Dropped: {total_gold:,} gp\n"
                f"Average per Monster: {avg_per_monster:,} gp\n\n"
                f"CR {cr} × {num_monsters} monster(s)"
            )
            self.gold_result.configure(state='disabled')
        except ValueError:
            self.gold_result.configure(state='normal')
            self.gold_result.delete("1.0", tk.END)
            self.gold_result.insert(
                tk.END,
                "❌ Error:\n\n"
                "Please enter valid numbers for\nCR and monster count."
            )
            self.gold_result.configure(state='disabled')
            
    def calculate_price(self):
        """Calculate item price based on rarity and condition."""
        rarity = self.rarity_var.get()
        condition = self.condition_var.get()
        
        if rarity and condition:
            base_price, adjusted_price = self.price_calc.calculate_price(rarity, condition)
            condition_percent = int(item_condition_mapping[condition] * 100)
            
            # Get display names
            rarity_display = rarity.replace("_", " ").title()
            condition_display = condition.replace("_", " ").title()
            
            self.price_result.configure(state='normal')
            self.price_result.delete("1.0", tk.END)
            self.price_result.insert(
                tk.END,
                f"💎 Price Calculation:\n\n"
                f"Base Price (Mint): {base_price:,} gp\n"
                f"Condition: {condition_display} ({condition_percent}%)\n"
                f"Adjusted Price: {adjusted_price:,} gp\n\n"
                f"Item: {rarity_display}"
            )
            self.price_result.configure(state='disabled')
        else:
            self.price_result.configure(state='normal')
            self.price_result.delete("1.0", tk.END)
            self.price_result.insert(
                tk.END,
                "❌ Error:\n\n"
                "Please select both rarity\nand condition."
            )
            self.price_result.configure(state='disabled')