"""
Shop Generator tab UI.
"""

import tkinter as tk
from tkinter import ttk
from core.shop_generator import ShopGenerator
from ui.components import OutputDisplay


class ShopTab:
    """Tab for generating shop inventories."""
    
    def __init__(self, parent):
        self.parent = parent
        self.generator = ShopGenerator()
        self.create_widgets()
        
    def create_widgets(self):
        """Create all widgets for the shop tab."""
        # Main container
        main_frame = ttk.Frame(self.parent, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure custom styles
        self.setup_styles()
        
        # Top section - Shop type buttons
        self.create_shop_buttons(main_frame)
        
        # Bottom section - Output display
        output_frame = ttk.LabelFrame(main_frame, text="🏪 Shop Inventory", padding="10", style='Shop.TLabelframe')
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        self.output_display = OutputDisplay(output_frame)
        
    def setup_styles(self):
        """Configure custom styles for better appearance."""
        style = ttk.Style()
        
        # Configure custom colors
        style.configure('Shop.TLabelframe', background='#f0f0f0')
        style.configure('Shop.TLabelframe.Label', background='#f0f0f0', font=('Segoe UI', 10, 'bold'))
        
        # Shop button styles
        style.configure('Shop.TButton', font=('Segoe UI', 10))
        style.map('Shop.TButton',
                  foreground=[('active', '#ffffff')],
                  background=[('active', '#0078d4')])
                  
    def create_shop_buttons(self, parent):
        """Create shop generation buttons."""
        button_frame = ttk.LabelFrame(parent, text="🎯 Generate Shop Inventory", padding="15", style='Shop.TLabelframe')
        button_frame.pack(fill=tk.X)
        
        # Create a grid of buttons with icons
        buttons_data = [
            ("✨ Magic Items Shop", self.generate_magic_items, 0, 0, "Generate a shop full of magical items"),
            ("📜 Spell Scrolls Shop", self.generate_scrolls, 0, 1, "Generate spell scrolls for sale"),
            ("🧪 Potion Shop", self.generate_potions, 0, 2, "Generate various potions and elixirs"),
            ("⚔️ Basic Items Shop", self.generate_basic, 1, 0, "Generate basic adventuring gear"),
            ("🎰 Combined Shop", self.generate_combined, 1, 1, "Generate a mixed inventory"),
        ]
        
        # Configure grid columns for equal spacing
        for i in range(3):
            button_frame.columnconfigure(i, weight=1, minsize=200)
        
        for text, command, row, col, tooltip in buttons_data:
            # Button container for padding
            btn_container = ttk.Frame(button_frame)
            btn_container.grid(row=row, column=col, padx=10, pady=8, sticky="ew")
            
            btn = ttk.Button(
                btn_container,
                text=text,
                command=command,
                style="Shop.TButton",
                width=25
            )
            btn.pack(fill=tk.X)
            
            # Create tooltip
            self.create_tooltip(btn, tooltip)
        
        # Add separator
        separator = ttk.Separator(button_frame, orient='horizontal')
        separator.grid(row=2, column=0, columnspan=3, sticky='ew', pady=(15, 10))
        
        # Add description with icon
        desc_label = ttk.Label(
            button_frame,
            text="💡 Click a button to generate shop inventory. Results are formatted for Discord.",
            font=('Segoe UI', 9, 'italic'),
            foreground='#666666'
        )
        desc_label.grid(row=3, column=0, columnspan=3, pady=(0, 5))
        
    def create_tooltip(self, widget, text):
        """Create a tooltip for a widget."""
        def on_enter(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = ttk.Label(
                tooltip,
                text=text,
                background="#ffffe0",
                relief=tk.SOLID,
                borderwidth=1,
                font=('Segoe UI', 9)
            )
            label.pack()
            
            widget.tooltip = tooltip
            
        def on_leave(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                del widget.tooltip
                
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
        
    def generate_magic_items(self):
        """Generate magic items shop inventory."""
        result = self.generator.stock_magic_items_shop()
        self.output_display.display_shop_results(result)
        
    def generate_scrolls(self):
        """Generate spell scrolls shop inventory."""
        result = self.generator.stock_scroll_shop()
        self.output_display.display_shop_results(result)
        
    def generate_potions(self):
        """Generate potions shop inventory."""
        result = self.generator.stock_potion_shop()
        self.output_display.display_shop_results(result)
        
    def generate_basic(self):
        """Generate basic items shop inventory."""
        result = self.generator.stock_basic_shop()
        self.output_display.display_shop_results(result)
        
    def generate_combined(self):
        """Generate combined shop inventory."""
        result = self.generator.stock_combined_shop()
        self.output_display.display_shop_results(result)