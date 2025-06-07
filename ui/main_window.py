"""
Main window UI for the D&D Item Generator application.
"""

import tkinter as tk
from tkinter import ttk
from ui.magic_item_tab import MagicItemTab
from ui.shop_tab import ShopTab
from ui.calculator_tab import CalculatorTab
from ui.styles import configure_styles


class MainApplication:
    """Main application window with tabbed interface."""
    
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_notebook()
        
    def setup_window(self):
        """Configure the main window."""
        self.root.title("D&D Item Generator")
        self.root.geometry("1200x800")
        
        # Configure styles
        configure_styles()
        
        # Set minimum window size
        self.root.minsize(1000, 700)
        
        # Center window on screen
        self.center_window()
        
    def center_window(self):
        """Center the window on the screen."""
        self.root.update_idletasks()
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Get window dimensions
        window_width = 1200
        window_height = 800
        
        # Calculate position
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
    def create_notebook(self):
        """Create the tabbed interface."""
        # Create main container
        main_container = ttk.Frame(self.root, padding="10")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create title label
        title_label = ttk.Label(
            main_container, 
            text="D&D Item Generator", 
            style="Title.TLabel"
        )
        title_label.pack(pady=(0, 10))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_tabs()
        
    def create_tabs(self):
        """Create all application tabs."""
        # Magic Item Generator tab
        magic_item_frame = ttk.Frame(self.notebook)
        self.notebook.add(magic_item_frame, text="Magic Item Generator")
        MagicItemTab(magic_item_frame)
        
        # Shop Generator tab
        shop_frame = ttk.Frame(self.notebook)
        self.notebook.add(shop_frame, text="Shop Generator")
        ShopTab(shop_frame)
        
        # Calculator tab
        calculator_frame = ttk.Frame(self.notebook)
        self.notebook.add(calculator_frame, text="Gold & Price Calculator")
        CalculatorTab(calculator_frame)
