"""
UI styling configuration for the application.
"""

from tkinter import ttk


def configure_styles():
    """Configure ttk styles for the entire application."""
    style = ttk.Style()
    
    # Configure general styles
    style.configure('TLabel', font=('Segoe UI', 10))
    style.configure('Title.TLabel', font=('Segoe UI', 16, 'bold'))
    style.configure('Heading.TLabel', font=('Segoe UI', 12, 'bold'))
    style.configure('TButton', font=('Segoe UI', 10), padding=8)
    style.configure('TEntry', font=('Segoe UI', 10), padding=5)
    style.configure('TCombobox', font=('Segoe UI', 10))
    
    # Configure frame styles
    style.configure('Card.TFrame', relief='solid', borderwidth=1)
    
    # Configure specific button styles
    style.configure('Primary.TButton', font=('Segoe UI', 11, 'bold'))
    style.configure('Generate.TButton', font=('Segoe UI', 10))
    
    # Map button states
    style.map('Primary.TButton',
              background=[('active', '#0078d4'),
                         ('!active', '#106ebe')])
    
    # Configure notebook tabs
    style.configure('TNotebook.Tab', padding=(20, 8))
