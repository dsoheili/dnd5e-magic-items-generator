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
        
        # Configure style
        self.setup_styles()
        
        # Create main layout - top controls, bottom output
        # Top frame for controls and reference
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Bottom frame for output (takes most space)
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.BOTH, expand=True)
        
        # In top frame: generators on left, reference on right
        generators_frame = ttk.Frame(top_frame)
        generators_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        reference_frame = ttk.Frame(top_frame)
        reference_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create the UI sections
        self.create_generators(generators_frame)
        self.create_reference(reference_frame)
        self.create_output(bottom_frame)
        
    def setup_styles(self):
        """Configure custom styles for better appearance."""
        style = ttk.Style()
        
        # Configure custom colors
        style.configure('Generator.TLabelframe', background='#f0f0f0')
        style.configure('Generator.TLabelframe.Label', background='#f0f0f0', font=('Segoe UI', 10, 'bold'))
        
        # Custom button styles
        style.configure('Generate.TButton', font=('Segoe UI', 9, 'bold'))
        style.map('Generate.TButton',
                  foreground=[('active', '#ffffff')],
                  background=[('active', '#0078d4')])
        
    def create_generators(self, parent):
        """Create side-by-side generator panels."""
        # Container for horizontal layout
        panels_container = ttk.Frame(parent)
        panels_container.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Item Generator
        item_frame = ttk.LabelFrame(panels_container, text="✨ Item Generator", padding="15", style='Generator.TLabelframe')
        item_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Character selection
        char_label = ttk.Label(item_frame, text="Character:", font=('Segoe UI', 9))
        char_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 8))
        self.character_var = tk.StringVar(value=character_names[0])
        char_combo = ttk.Combobox(
            item_frame,
            textvariable=self.character_var,
            values=character_names,
            state="readonly",
            width=18,
            font=('Segoe UI', 9)
        )
        char_combo.grid(row=0, column=1, sticky=tk.W, pady=(0, 8))
        
        # Table selection
        table_label = ttk.Label(item_frame, text="Table:", font=('Segoe UI', 9))
        table_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 8))
        self.table_var = tk.StringVar()
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
            item_frame,
            textvariable=self.table_var,
            values=table_options,
            state="readonly",
            width=20,
            font=('Segoe UI', 9)
        )
        table_combo.grid(row=1, column=1, sticky=tk.W, pady=(0, 8))
        
        # Row number
        row_label = ttk.Label(item_frame, text="Row:", font=('Segoe UI', 9))
        row_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 8))
        self.row_number_var = tk.StringVar()
        row_entry = ttk.Entry(item_frame, textvariable=self.row_number_var, width=10, font=('Segoe UI', 9))
        row_entry.grid(row=2, column=1, sticky=tk.W, pady=(0, 8))
        
        # Separator
        separator1 = ttk.Separator(item_frame, orient='horizontal')
        separator1.grid(row=3, column=0, columnspan=2, sticky='ew', pady=10)
        
        # Help text with icon
        help_label = ttk.Label(
            item_frame,
            text="💡 Leave empty for random generation",
            font=('Segoe UI', 8, 'italic'),
            foreground='#666666'
        )
        help_label.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        # Generate button
        generate_btn = ttk.Button(
            item_frame,
            text="🎲 Generate Magic Item",
            command=self.generate_item,
            style='Generate.TButton'
        )
        generate_btn.grid(row=5, column=0, columnspan=2, sticky=tk.W)
        
        # Right panel - Spell Generator
        spell_frame = ttk.LabelFrame(panels_container, text="📜 Spell Scroll Generator", padding="15", style='Generator.TLabelframe')
        spell_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Spell level selection
        spell_label = ttk.Label(spell_frame, text="Spell Level:", font=('Segoe UI', 9))
        spell_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 8))
        self.spell_level_var = tk.StringVar()
        
        spell_options = [
            "",  # Empty for random
            "Cantrip",
            "1st Level",
            "2nd Level",
            "3rd Level",
            "4th Level",
            "5th Level",
            "6th Level",
            "7th Level",
            "8th Level",
            "9th Level"
        ]
        
        spell_combo = ttk.Combobox(
            spell_frame,
            textvariable=self.spell_level_var,
            values=spell_options,
            state="readonly",
            width=15,
            font=('Segoe UI', 9)
        )
        spell_combo.grid(row=0, column=1, sticky=tk.W, pady=(0, 8))
        spell_combo.set("")  # Default to random
        
        # Separator
        separator2 = ttk.Separator(spell_frame, orient='horizontal')
        separator2.grid(row=1, column=0, columnspan=2, sticky='ew', pady=10)
        
        # Help text with icon
        spell_help = ttk.Label(
            spell_frame,
            text="💡 Leave empty for random level",
            font=('Segoe UI', 8, 'italic'),
            foreground='#666666'
        )
        spell_help.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        # Generate spell button
        generate_spell_btn = ttk.Button(
            spell_frame,
            text="🎲 Generate Spell Scroll",
            command=self.generate_spell,
            style='Generate.TButton'
        )
        generate_spell_btn.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        
        # Add some padding to make panels equal height
        spell_frame.grid_rowconfigure(4, weight=1)
        
    def create_reference(self, parent):
        """Create compact reference section."""
        ref_frame = ttk.LabelFrame(parent, text="📋 Quick Reference", padding="10", style='Generator.TLabelframe')
        ref_frame.pack(fill=tk.Y)
        
        # Reference text - height matches generator panels
        ref_text = tk.Text(
            ref_frame,
            wrap=tk.NONE,
            width=45,
            height=13,  # Adjusted to match panel height
            font=('Consolas', 9),
            relief=tk.GROOVE,
            background='#ffffff',
            borderwidth=1
        )
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(ref_frame, orient=tk.VERTICAL, command=ref_text.yview)
        ref_text.configure(yscrollcommand=scrollbar.set)
        
        ref_text.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        ref_text.insert(tk.END, gui_info_text)
        ref_text.configure(state='disabled')
        
    def create_output(self, parent):
        """Create output section that takes up most space."""
        output_frame = ttk.LabelFrame(parent, text="📤 Generated Output", padding="10", style='Generator.TLabelframe')
        output_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_display = OutputDisplay(output_frame)
        
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
        spell_selection = self.spell_level_var.get()
        
        # Handle random level
        if not spell_selection:
            import random
            spell_level = random.randint(0, 9)
        else:
            # Map spell level names to numbers
            level_mapping = {
                "Cantrip": 0,
                "1st Level": 1,
                "2nd Level": 2,
                "3rd Level": 3,
                "4th Level": 4,
                "5th Level": 5,
                "6th Level": 6,
                "7th Level": 7,
                "8th Level": 8,
                "9th Level": 9
            }
            spell_level = level_mapping.get(spell_selection, 0)
        
        # Generate spell
        result = self.generator.generate_random_spell(spell_level)
        
        # Display result
        self.output_display.display_result(
            result['output_text'],
            result.get('url', '')
        )