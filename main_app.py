#!/usr/bin/env python3
"""
D&D Item Generator - Main Application
A tool for generating magic items, calculating gold drops, and managing item shops for D&D games.

To run: Just double-click this file (main.py) or run: python main.py
"""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.main_window import MainApplication


def main():
    """Main entry point for the application."""
    try:
        root = tk.Tk()
        app = MainApplication(root)
        root.mainloop()
    except Exception as e:
        # If running by double-click, show error in a message box
        import tkinter.messagebox as messagebox
        messagebox.showerror("Error", f"An error occurred:\n\n{str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
