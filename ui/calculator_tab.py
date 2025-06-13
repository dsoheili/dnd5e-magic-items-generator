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
        desc.pack(anchor=tk.W, pady=(0, 5))
        
        # Instructions
        instructions = ttk.Label(
            calc_frame,
            text="Add monster groups with count and CR",
            font=('Segoe UI', 8),
            foreground='#888888'
        )
        instructions.pack(anchor=tk.W, pady=(0, 10))
        
        # Monster groups frame
        groups_container = ttk.LabelFrame(calc_frame, text="Monster Groups", padding="5")
        groups_container.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Scrollable frame for groups
        self.groups_canvas = tk.Canvas(groups_container, height=150, bg='#f0f0f0', highlightthickness=0)
        scrollbar = ttk.Scrollbar(groups_container, orient="vertical", command=self.groups_canvas.yview)
        self.groups_frame = ttk.Frame(self.groups_canvas)
        
        self.groups_frame.bind(
            "<Configure>",
            lambda e: self.groups_canvas.configure(scrollregion=self.groups_canvas.bbox("all"))
        )
        
        self.groups_canvas.create_window((0, 0), window=self.groups_frame, anchor="nw")
        self.groups_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Bind mouse wheel
        def _on_mousewheel(event):
            self.groups_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        self.groups_canvas.bind("<MouseWheel>", _on_mousewheel)
        self.groups_canvas.bind("<Enter>", lambda e: self.groups_canvas.bind_all("<MouseWheel>", _on_mousewheel))
        self.groups_canvas.bind("<Leave>", lambda e: self.groups_canvas.unbind_all("<MouseWheel>"))
        
        self.groups_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Store group entries
        self.monster_groups = []
        
        # Common CR values with display names
        self.cr_values = ["0", "1/8", "1/4", "1/2", "1", "2", "3", "4", "5", "6", "7", "8", 
                         "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                         "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
        
        # CR mapping for calculations
        self.cr_mapping = {
            "0": 0, "1/8": 0.125, "1/4": 0.25, "1/2": 0.5,
            "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
            "9": 9, "10": 10, "11": 11, "12": 12, "13": 13, "14": 14, "15": 15,
            "16": 16, "17": 17, "18": 18, "19": 19, "20": 20, "21": 21, "22": 22,
            "23": 23, "24": 24, "25": 25, "26": 26, "27": 27, "28": 28, "29": 29, "30": 30
        }
        
        # Add first group
        self.add_monster_group()
        
        # Buttons frame
        buttons_frame = ttk.Frame(calc_frame)
        buttons_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Add group button
        add_btn = ttk.Button(
            buttons_frame,
            text="➕ Add Group",
            command=self.add_monster_group,
            width=15
        )
        add_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Calculate button
        calc_btn = ttk.Button(
            buttons_frame,
            text="🎲 Calculate",
            command=self.calculate_gold,
            style='Calculate.TButton',
            width=15
        )
        calc_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Clear button
        clear_btn = ttk.Button(
            buttons_frame,
            text="Clear",
            command=self.clear_monster_groups,
            width=10
        )
        clear_btn.pack(side=tk.LEFT)
        
        # Result display - more spacious
        result_frame = ttk.LabelFrame(calc_frame, text="📊 Result", padding="15")
        result_frame.pack(fill=tk.BOTH, pady=(15, 0))
        
        self.gold_result = tk.Text(
            result_frame,
            height=4,
            width=40,
            font=('Segoe UI', 12),
            wrap=tk.WORD,
            relief=tk.FLAT,
            background='#f8f8f8',
            borderwidth=0
        )
        self.gold_result.pack(fill=tk.BOTH, padx=5, pady=5)
        
        # Breakdown display (smaller, for DM eyes only)
        breakdown_frame = ttk.LabelFrame(calc_frame, text="Calculation Breakdown", padding="10")
        breakdown_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.breakdown_text = tk.Text(
            breakdown_frame,
            height=6,
            width=40,
            font=('Segoe UI', 9),
            wrap=tk.WORD,
            relief=tk.FLAT,
            background='#f5f5f5',
            foreground='#666666',
            borderwidth=0
        )
        self.breakdown_text.pack(fill=tk.X)
        
        # Default text
        self.gold_result.insert(tk.END, "Add monster groups and click Calculate.")
        self.gold_result.configure(state='disabled')
        self.breakdown_text.configure(state='disabled')
        
    def add_monster_group(self):
        """Add a new monster group entry."""
        # Compact frame
        group_frame = ttk.Frame(self.groups_frame)
        group_frame.pack(fill=tk.X, padx=5, pady=3)
        
        # Count label and spinbox
        ttk.Label(group_frame, text="Count:", font=('Segoe UI', 9)).pack(side=tk.LEFT, padx=(5, 3))
        
        count_var = tk.StringVar(value="1")
        count_spin = ttk.Spinbox(
            group_frame,
            from_=1,
            to=999,
            textvariable=count_var,
            width=8,
            font=('Segoe UI', 9)
        )
        count_spin.pack(side=tk.LEFT, padx=(0, 10))
        
        # CR label and dropdown
        ttk.Label(group_frame, text="CR:", font=('Segoe UI', 9)).pack(side=tk.LEFT, padx=(0, 3))
        
        cr_var = tk.StringVar(value="1")
        cr_combo = ttk.Combobox(
            group_frame,
            textvariable=cr_var,
            values=self.cr_values,
            state="readonly",
            width=8,
            font=('Segoe UI', 9)
        )
        cr_combo.pack(side=tk.LEFT, padx=(0, 10))
        
        # Small remove button
        remove_btn = tk.Button(
            group_frame,
            text="✕",
            command=lambda: self.remove_monster_group(group_frame),
            font=('Segoe UI', 8),
            fg='red',
            bg='#f0f0f0',
            bd=1,
            padx=2,
            pady=0
        )
        remove_btn.pack(side=tk.LEFT)
        
        # Store the group
        self.monster_groups.append({
            'frame': group_frame,
            'count_var': count_var,
            'cr_var': cr_var
        })
        
    def remove_monster_group(self, frame):
        """Remove a monster group."""
        # Find and remove from list
        self.monster_groups = [g for g in self.monster_groups if g['frame'] != frame]
        # Destroy the frame
        frame.destroy()
        
    def clear_monster_groups(self):
        """Clear all monster groups."""
        for group in self.monster_groups:
            group['frame'].destroy()
        self.monster_groups = []
        # Add one empty group
        self.add_monster_group()
        
    def calculate_gold(self):
        """Calculate gold drop based on all monster groups."""
        try:
            total_gold = 0
            valid_groups = 0
            breakdown = []
            
            for group in self.monster_groups:
                count_str = group['count_var'].get().strip()
                cr_str = group['cr_var'].get().strip()
                
                if count_str and cr_str:
                    count = int(count_str)
                    # Use the mapping to convert display value to actual CR
                    if cr_str in self.cr_mapping:
                        cr_value = self.cr_mapping[cr_str]
                    else:
                        cr_value = float(cr_str)  # Fallback for any unmapped values
                    
                    # Calculate gold for this group
                    group_gold = self.gold_calc.calculate_drop(cr_value, count)
                    total_gold += group_gold
                    valid_groups += 1
                    
                    # Add to breakdown
                    avg_per_monster = group_gold // count if count > 0 else 0
                    breakdown.append(f"{count}x CR {cr_str}: {group_gold:,} gp (avg {avg_per_monster:,} gp each)")
            
            if valid_groups == 0:
                raise ValueError("No valid monster groups")
            
            # Update main result
            self.gold_result.configure(state='normal')
            self.gold_result.delete("1.0", tk.END)
            self.gold_result.insert(
                tk.END,
                f"**Encounter Rewards**\n\n"
                f"Gold Found: {total_gold:,} gp"
            )
            self.gold_result.configure(state='disabled')
            
            # Update breakdown
            self.breakdown_text.configure(state='normal')
            self.breakdown_text.delete("1.0", tk.END)
            breakdown_str = "\n".join(breakdown)
            self.breakdown_text.insert(tk.END, f"Breakdown by group:\n\n{breakdown_str}\n\nTotal: {total_gold:,} gp")
            self.breakdown_text.configure(state='disabled')
            
        except ValueError as e:
            self.gold_result.configure(state='normal')
            self.gold_result.delete("1.0", tk.END)
            self.gold_result.insert(
                tk.END,
                "❌ Error:\n\n"
                "Please enter valid numbers for\ncount and CR in at least one group."
            )
            self.gold_result.configure(state='disabled')
            
            self.breakdown_text.configure(state='normal')
            self.breakdown_text.delete("1.0", tk.END)
            self.breakdown_text.configure(state='disabled')
        
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