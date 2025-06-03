import tkinter as tk
from tkinter import ttk
from common.common_methods import *
from config.config import *

def calculate_gp_drop(cr, num_monsters):
    """Calculate gold drop for monsters using simple ranges"""
    total_gp = 0
    
    # Find the appropriate range for this CR
    min_gold, max_gold = get_gold_range_for_cr(cr)
    
    for _ in range(num_monsters):
        gp_drop = random.randint(min_gold, max_gold)
        total_gp += gp_drop
    
    return total_gp

def get_gold_range_for_cr(cr):
    """Get gold range for a specific CR, with fallback logic"""
    # Direct match first
    if cr in gold_drop_by_cr:
        return gold_drop_by_cr[cr]
    
    # Find closest CR if exact match not found
    available_crs = sorted(gold_drop_by_cr.keys())
    
    if cr < available_crs[0]:
        return gold_drop_by_cr[available_crs[0]]
    elif cr > available_crs[-1]:
        return gold_drop_by_cr[available_crs[-1]]
    else:
        # Find the closest CR
        closest_cr = min(available_crs, key=lambda x: abs(x - cr))
        return gold_drop_by_cr[closest_cr]

def submit_cr():
    try:
        cr = float(cr_entry.get())
        num_monsters = int(num_monsters_entry.get())
        gp_drop = calculate_gp_drop(cr, num_monsters)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Total Gold Dropped: {gp_drop} gp")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid CR and number of monsters.")

def appraise_item():
    rarity_key = rarity_var.get()
    condition = condition_var.get()
    if rarity_key and condition:
        price = get_item_price(rarity_key)
        adjusted_price = int(price * item_condition_mapping[condition])
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Perfect condition price: {price} gp,\nOffered price: {adjusted_price} gp")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please select both rarity and condition.")

root = tk.Tk()
root.title("Item and CR Price Calculator")
root.geometry("500x450")  # Increased window height

style = ttk.Style()
style.configure('TLabel', font=('Arial', 10), padding=5)
style.configure('TButton', font=('Arial', 10), padding=5)
style.configure('TEntry', font=('Arial', 10), padding=5)

rarity_var = tk.StringVar()
ttk.Label(root, text="Select item rarity:", style='TLabel').pack(pady=(10, 0))
ttk.OptionMenu(root, rarity_var, None, *price_ranges.keys()).pack(fill='x', padx=15)

condition_var = tk.StringVar(value="mint")
ttk.Label(root, text="Select item condition:", style='TLabel').pack()
ttk.OptionMenu(root, condition_var, "mint", *item_condition_mapping.keys()).pack(fill='x', padx=15)

ttk.Button(root, text="Calculate Item Price", command=appraise_item).pack(pady=(10, 5))

ttk.Label(root, text="Enter Challenge Rating (CR):", style='TLabel').pack()
cr_entry = ttk.Entry(root, style='TEntry')
cr_entry.pack(fill='x', padx=15)

ttk.Label(root, text="Enter Number of Monsters:", style='TLabel').pack()
num_monsters_entry = ttk.Entry(root, style='TEntry')
num_monsters_entry.pack(fill='x', padx=15)

ttk.Button(root, text="Calculate GP Drop", command=submit_cr).pack(pady=10)

result_text = tk.Text(root, height=4, width=40, font=('Arial', 10), padx=10, pady=10)
result_text.pack(pady=10, fill='x', padx=15)

root.mainloop()
