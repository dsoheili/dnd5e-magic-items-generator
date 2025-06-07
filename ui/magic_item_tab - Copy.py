"""
Magic Item Generator tab UI.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from core.item_generator import ItemGenerator
from ui.components import OutputDisplay
from config.config import character_names, gui_info_text


class MagicItemTab:
    """Tab for generating individual magic items."""
    
    def __init__(self, parent):
        self.parent = parent
        self.generator = ItemGenerator()
        self.create_widgets()
        
    def create_widgets(self):
        """Create all widgets for the magic item tab."""
        # Main container
        main_frame = ttk.Frame(self.parent, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create two columns
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Left column - Input controls
        self.create_input_controls(left_frame)
        
        # Right column - Reference information
        self.create_reference_info(right_frame)
        
        # Bottom - Output display
        output_frame = ttk.LabelFrame(main_frame, text="Generated Item", padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.output_display = OutputDisplay(output_frame)
        
    def create_input_controls(self, parent):
        """Create input controls for item generation."""
        # Character selection
        char_frame = ttk.LabelFrame(parent, text="Character", padding="10")
        char_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(char_frame, text="Select Character:").pack(anchor=tk.W)
        self.character_var = tk.StringVar(value=character_names[0])
        char_combo = ttk.Combobox(
            char_frame, 
            textvariable=self.character_var,
            values=character_names,
            state="readonly",
            width=30
        )
        char_combo.pack(fill=tk.X, pady=(5, 0))
        
        # Generation options
        options_frame = ttk.LabelFrame(parent, text="Generation Options", padding="10")
        options_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Table selection dropdown
        ttk.Label(options_frame, text="Table (optional):").pack(anchor=tk.W)
        self.table_var = tk.StringVar()
        
        # Create table options with letter and rarity
        table_options = [
            "",  # Empty for random
            "A - Common",
            "B - Uncommon, minor",
            "C - Rare, minor",
            "D - Very Rare, minor",
            "E - Legendary, minor",
            "F - Uncommon, major",
            "G - Rare, major",
            "H - Very Rare, major",
            "I - Legendary, major",
            "J - Mythic",
            "K - Unknown"
        ]
        
        table_combo = ttk.Combobox(
            options_frame,
            textvariable=self.table_var,
            values=table_options,
            state="readonly",
            width=30
        )
        table_combo.pack(fill=tk.X, pady=(5, 10))
        
        # Row number
        ttk.Label(options_frame, text="Row Number (optional):").pack(anchor=tk.W)
        self.row_number_var = tk.StringVar()
        row_entry = ttk.Entry(options_frame, textvariable=self.row_number_var)
        row_entry.pack(fill=tk.X, pady=(5, 10))
        
        # Help text
        help_text = ttk.Label(
            options_frame,
            text="Leave fields empty for random generation",
            font=('Segoe UI', 9, 'italic')
        )
        help_text.pack(anchor=tk.W)
        
        # Generate button
        generate_btn = ttk.Button(
            parent,
            text="Generate Magic Item",
            command=self.generate_item,
            style="Primary.TButton"
        )
        generate_btn.pack(fill=tk.X, pady=(10, 0))
        
        # Spell Generator section
        spell_frame = ttk.LabelFrame(parent, text="Spell Generator", padding="10")
        spell_frame.pack(fill=tk.X, pady=(20, 0))
        
        ttk.Label(spell_frame, text="Spell Level:").pack(anchor=tk.W)
        self.spell_level_var = tk.StringVar()
        spell_combo = ttk.Combobox(
            spell_frame,
            textvariable=self.spell_level_var,
            values=[str(i) for i in range(10)],  # 0-9
            state="readonly",
            width=10
        )
        spell_combo.pack(anchor=tk.W, pady=(5, 10))
        spell_combo.set("1")  # Default to level 1
        
        generate_spell_btn = ttk.Button(
            spell_frame,
            text="Generate Random Spell",
            command=self.generate_spell
        )
        generate_spell_btn.pack(fill=tk.X)
        
    def create_reference_info(self, parent):
        """Create reference information display."""
        ref_frame = ttk.LabelFrame(parent, text="Reference Table", padding="10")
        ref_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create scrolled text widget for reference
        ref_text = scrolledtext.ScrolledText(
            ref_frame,
            wrap=tk.NONE,
            width=65,
            height=25,
            font=('Consolas', 10)
        )
        ref_text.pack(fill=tk.BOTH, expand=True)
        ref_text.insert(tk.END, gui_info_text)
        ref_text.configure(state='disabled')
        
    def generate_item(self):
        """Generate a magic item based on current inputs."""
        character_name = self.character_var.get()
        table_selection = self.table_var.get()
        row_number = self.row_number_var.get()
        
        # Map table letter to number
        table_mapping = {
            "A - Common": 1,
            "B - Uncommon, minor": 2,
            "C - Rare, minor": 3,
            "D - Very Rare, minor": 4,
            "E - Legendary, minor": 5,
            "F - Uncommon, major": 6,
            "G - Rare, major": 7,
            "H - Very Rare, major": 8,
            "I - Legendary, major": 9,
            "J - Mythic": 10,
            "K - Unknown": 11
        }
        
        # Get table number from selection
        table_num = table_mapping.get(table_selection) if table_selection else None
        row_num = int(row_number) if row_number else None
        
        # Generate item
        result = self.generator.generate_magic_item(
            character_name=character_name,
            table_number=table_num,
            row_number=row_num
        )
        
        # Display result
        self.output_display.display_result(
            result['output_text'],
            result.get('url', '')
        )
        
    def generate_spell(self):
        """Generate a random spell of the selected level."""
        spell_level = self.spell_level_var.get()
        
        if spell_level:
            # Generate spell
            result = self.generator.generate_random_spell(int(spell_level))
            
            # Display result
            self.output_display.display_result(
                result['output_text'],
                result.get('url', '')
            )
