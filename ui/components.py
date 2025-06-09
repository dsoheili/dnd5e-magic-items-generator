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
        self.right_frame = None  # Initialize as None
        self.links_frame = None
        self.create_widgets()
        
    def create_widgets(self):
        """Create the output display widgets."""
        # Create main styled container
        style = ttk.Style()
        style.configure('Output.TLabelframe', background='#f0f0f0')
        style.configure('Output.TLabelframe.Label', background='#f0f0f0', font=('Segoe UI', 10, 'bold'))
        
        main_frame = ttk.LabelFrame(self.parent, text="📤 Generated Output", padding="10", style='Output.TLabelframe')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Store references
        self.main_container = self.parent
        self.main_frame = main_frame
        
        # Create horizontal paned window for side-by-side layout
        self.paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Left side - Discord output
        left_frame = ttk.Frame(self.paned_window)
        self.paned_window.add(left_frame, weight=3)
        
        discord_frame = ttk.LabelFrame(left_frame, text="Discord Output (Copy/Paste)", padding="5")
        discord_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create scrolled text widget
        self.output_text = scrolledtext.ScrolledText(
            discord_frame,
            wrap=tk.WORD,
            width=60,
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
        
        # Right side will be created when needed
        self.left_frame = left_frame  # Store reference
        
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
        valid_urls = [url for url in urls if url and url.strip()]
        
        if valid_urls:
            self.show_links(valid_urls)
        else:
            self.hide_links()
            
    def show_links(self, urls):
        """Display clickable links."""
        # Filter out empty URLs
        valid_urls = [url for url in urls if url and url.strip()]
        
        if not valid_urls:
            self.hide_links()
            return
        
        # Clean up any existing right frame
        self.cleanup_right_frame()
        
        # Create fresh right frame
        self.right_frame = ttk.Frame(self.paned_window)
        self.paned_window.add(self.right_frame, weight=2)
        
        # Create links frame
        self.links_frame = ttk.LabelFrame(self.right_frame, text="🔗 Quick Links", padding="10")
        self.links_frame.pack(fill=tk.BOTH, expand=True)
        
        # For single URL (Magic Item Generator)
        if len(valid_urls) == 1:
            url = valid_urls[0]
            
            # Extract item name
            item_name = self.extract_item_name(url)
            
            # Create centered frame
            center_frame = ttk.Frame(self.links_frame)
            center_frame.pack(expand=True)
            
            # Create nice button
            link_btn = ttk.Button(
                center_frame,
                text=item_name,
                command=lambda: webbrowser.open(url),
                style='Generate.TButton'
            )
            link_btn.pack(pady=20, padx=20)
            
            # Add description
            desc_label = ttk.Label(
                center_frame,
                text="Click to view item details",
                font=('Segoe UI', 9, 'italic'),
                foreground='#666666'
            )
            desc_label.pack()
            
        else:
            # Multiple URLs (Shop Generator)
            # Create scrolled frame with proper space
            canvas = tk.Canvas(self.links_frame, bg='#f0f0f0', highlightthickness=0)
            scrollbar = ttk.Scrollbar(self.links_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            
            # Configure canvas
            canvas.configure(yscrollcommand=scrollbar.set)
            
            # Bind mouse wheel
            def _on_mousewheel(event):
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")
                
            # Bind to canvas and all children
            canvas.bind("<MouseWheel>", _on_mousewheel)
            canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
            canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
            
            # Update canvas window width when canvas is resized
            def configure_canvas(event):
                canvas.itemconfig(canvas_window, width=event.width)
                
            canvas.bind('<Configure>', configure_canvas)
            
            # Create item buttons - one per row for clarity
            for i, url in enumerate(valid_urls):
                item_name = self.extract_item_name(url)
                
                # Create frame for each item
                item_frame = ttk.Frame(scrollable_frame, relief=tk.RIDGE, borderwidth=1)
                item_frame.pack(fill=tk.X, padx=10, pady=5)
                
                # Item button
                link_btn = ttk.Button(
                    item_frame,
                    text=f"{i+1}. {item_name}",
                    command=lambda u=url: webbrowser.open(u)
                )
                link_btn.pack(fill=tk.X, padx=10, pady=10)
            
            # Pack canvas and scrollbar
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            # Add count label
            count_label = ttk.Label(
                self.links_frame,
                text=f"{len(valid_urls)} items with links",
                font=('Segoe UI', 9, 'italic'),
                foreground='#666666'
            )
            count_label.pack(pady=(5, 0))
                
    def cleanup_right_frame(self):
        """Completely remove and destroy the right frame."""
        if self.right_frame and self.right_frame.winfo_exists():
            try:
                # Remove from paned window
                if self.right_frame in self.paned_window.panes():
                    self.paned_window.remove(self.right_frame)
                # Destroy the frame
                self.right_frame.destroy()
            except:
                pass  # Frame already destroyed
                
        # Reset references
        self.right_frame = None
        self.links_frame = None
        
    def hide_links(self):
        """Hide the links section."""
        self.cleanup_right_frame()
            
    def extract_item_name(self, url):
        """Extract a clean item name from URL."""
        item_name = "Unknown Item"
        
        if "dndbeyond.com" in url and "magic-items" in url:
            # Extract from D&D Beyond URL
            parts = url.split("/")
            if len(parts) >= 2:
                raw_name = parts[-1]
                # Remove ID prefix if present (e.g., "215718-ring-of-protection")
                if "-" in raw_name and raw_name.split("-")[0].isdigit():
                    raw_name = "-".join(raw_name.split("-")[1:])
                item_name = raw_name.replace("-", " ").title()
        elif "/" in url:
            # Generic URL parsing
            item_name = url.split("/")[-1].replace("-", " ").replace("_", " ").title()
            
        return item_name
            
    def copy_to_clipboard(self):
        """Copy the output text to clipboard."""
        text = self.output_text.get("1.0", tk.END).strip()
        if text:
            self.main_container.clipboard_clear()
            self.main_container.clipboard_append(text)
            self.show_copy_success()
            
    def show_copy_success(self):
        """Show a temporary success message."""
        success_label = ttk.Label(
            self.left_frame,
            text="✓ Copied to clipboard!",
            foreground="green",
            font=('Segoe UI', 10, 'bold')
        )
        success_label.pack()
        self.main_container.after(2000, success_label.destroy)