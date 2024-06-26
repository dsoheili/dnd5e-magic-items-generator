import tkinter as tk
from tkinter import ttk
from common.common_methods import *
from config.config import *

def calculate_gp_drop(cr, num_monsters):
    total_gp = 0
    for _ in range(num_monsters):
        if cr == 0:
            gp_drop = roll_multiple_dice(1, 10, 0)
        elif 0.125 <= cr <= 0.5:
            gp_drop = roll_multiple_dice(2, 10, 5)
        elif cr == 1:
            gp_drop = roll_multiple_dice(4, 10, 10)
        elif 2 <= cr <= 3:
            gp_drop = roll_multiple_dice(6, 20, 30)
        elif 4 <= cr <= 5:
            gp_drop = roll_multiple_dice(8, 50, 100)
        elif 6 <= cr <= 10:
            gp_drop = roll_multiple_dice(10, 100, 200)
        elif 11 <= cr <= 15:
            gp_drop = roll_multiple_dice(15, 100, 500)
        elif 16 <= cr <= 20:
            gp_drop = roll_multiple_dice(20, 100, 1000)
        elif cr >= 21:
            gp_drop = roll_multiple_dice(25, 200, 2000)
        total_gp += gp_drop
    return total_gp

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
