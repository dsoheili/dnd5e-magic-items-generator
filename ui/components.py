"""
Reusable UI components.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import webbrowser


class OutputDisplay:
    """Reusable output display component with Discord formatting and clickable links."""
    
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()
        
    def create_widgets(self):
        """Create the output display widgets."""
        # Create container frame
        container = ttk.Frame(self.parent)
        container.pack(fill=tk.BOTH, expand=True)
        
        # Discord output section
        discord_frame = ttk.LabelFrame(container, text="Discord Output (Copy/Paste)", padding="5")
        discord_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create scrolled text widget
        self.output_text = scrolledtext.ScrolledText(
            discord_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=('Consolas', 11)
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Copy button
        copy_btn = ttk.Button(
            discord_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard
        )
        copy_btn.pack(pady=(5, 0))
        
        # Links section
        self.links_frame = ttk.LabelFrame(container, text="Quick Links", padding="5")
        self.links_container = None
        self.links_canvas = None
        self.links_scrollbar = None
        
    def display_result(self, text, url=None):
        """Display single item result."""
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)
        
        # Handle URL if provided
        if url and url.strip():
            self.show_links([url])
        else:
            self.hide_links()
            
    def display_shop_results(self, results):
        """Display shop results with multiple items."""
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, results['output_text'])
        
        # Show links if any
        urls = results.get('urls', [])
        # Filter out empty strings and None values
        valid_urls = [url for url in urls if url and url.strip()]
        
        if valid_urls:
            self.show_links(valid_urls)
        else:
            self.hide_links()
            
    def show_links(self, urls):
        """Display clickable links."""
        # Clear existing links widgets
        if self.links_canvas:
            self.links_canvas.destroy()
        if self.links_scrollbar:
            self.links_scrollbar.destroy()
        if self.links_container:
            self.links_container.destroy()
            
        # Filter out empty URLs
        valid_urls = [url for url in urls if url and url.strip()]
        
        if not valid_urls:
            self.hide_links()
            return
            
        self.links_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Create scrollable frame for links
        self.links_canvas = tk.Canvas(self.links_frame, height=min(150, len(valid_urls) * 35))
        self.links_scrollbar = ttk.Scrollbar(self.links_frame, orient="vertical", command=self.links_canvas.yview)
        self.links_container = ttk.Frame(self.links_canvas)
        
        self.links_canvas.configure(yscrollcommand=self.links_scrollbar.set)
        canvas_frame = self.links_canvas.create_window((0, 0), window=self.links_container, anchor="nw")
        
        self.links_canvas.pack(side="left", fill="both", expand=True)
        self.links_scrollbar.pack(side="right", fill="y")
        
        # Create link buttons in a grid (2 columns for space efficiency)
        for i, url in enumerate(valid_urls):
            # Extract item name from URL or use generic label
            label = f"Link {i+1}"
            if "/" in url:
                parts = url.split("/")[-1].replace("-", " ").title()
                label = parts[:35] + "..." if len(parts) > 35 else parts
                    
            link_btn = ttk.Button(
                self.links_container,
                text=label,
                command=lambda u=url: webbrowser.open(u)
            )
            row = i // 2
            col = i % 2
            link_btn.grid(row=row, column=col, padx=5, pady=2, sticky="ew")
        
        # Configure grid weights
        self.links_container.columnconfigure(0, weight=1)
        self.links_container.columnconfigure(1, weight=1)
        
        # Update scroll region
        self.links_container.update_idletasks()
        self.links_canvas.configure(scrollregion=self.links_canvas.bbox("all"))
                
    def hide_links(self):
        """Hide the links section."""
        self.links_frame.pack_forget()
        
    def copy_to_clipboard(self):
        """Copy the output text to clipboard."""
        text = self.output_text.get("1.0", tk.END).strip()
        if text:
            self.parent.clipboard_clear()
            self.parent.clipboard_append(text)
            
            # Show temporary success message
            self.show_copy_success()
            
    def show_copy_success(self):
        """Show a temporary success message."""
        success_label = ttk.Label(
            self.parent,
            text="✓ Copied to clipboard!",
            foreground="green",
            font=('Segoe UI', 10, 'bold')
        )
        success_label.pack()
        
        # Remove after 2 seconds
        self.parent.after(2000, success_label.destroy)
