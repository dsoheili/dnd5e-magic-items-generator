# D&D 5e Magic Items Generator

A comprehensive tool for Dungeons & Dragons 5th Edition game masters to generate magic items, manage shop inventories, and calculate treasure rewards. Features a GUI with Discord-friendly output formatting.

## Features

### 🎲 Magic Item Generator
- Generate random magic items based on rarity tables (A-K)
- Optional specific table and row selection
- Character assignment for found items
- Quick reference table for rarity distributions
- Integrated spell scroll generator with pricing

### 🏪 Shop Generator
- **Magic Items Shop** - Generate magical item inventories
- **Spell Scrolls Shop** - Create spell scroll selections
- **Potion Shop** - Stock various potions and elixirs
- **Basic Items Shop** - Generate adventuring gear
- **Combined Shop** - Mixed inventory generation

### 💰 Calculators
- **Gold Drop Calculator** - Calculate treasure from defeated monsters based on CR
- **Item Price Calculator** - Determine item values based on rarity and condition

### 🔗 Additional Features
- Discord-formatted output (copy/paste ready)
- Clickable URL links for items with online references
- One-click copy to clipboard

## Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)

### Setup
1. Clone or download this repository
2. Run the application with run_dnd_generator.bat or:
   ```bash
   python main_app.py
   ```

## Project Structure

```
dnd-item-generator/
│
├── main.py                    # Application entry point
│
├── common/                    # Common utilities
│   ├── common_methods.py      # Utility functions
│   └── magic_item_properties.py  # Item property definitions
│
├── config/                    # Configuration
│   └── config.py             # Application settings
│
├── core/                     # Core business logic
│   ├── item_generator.py     # Magic item generation
│   ├── shop_generator.py     # Shop inventory generation
│   └── calculators.py        # Gold and price calculations
│
├── ui/                       # User interface
│   ├── main_window.py        # Main application window
│   ├── magic_item_tab.py     # Item generator tab
│   ├── shop_tab.py           # Shop generator tab
│   ├── calculator_tab.py     # Calculator tab
│   ├── components.py         # Reusable UI components
│   └── styles.py             # UI styling
│
└── data/                     # Data files (CSV format)
    ├── basic.csv
    ├── common.csv
    ├── uncommon_minor.csv
    ├── rare_minor.csv
    ├── legendary_minor.csv
    ├── magic_items_data.txt   # Item URLs
    ├── spells/               # Spell data by level
    └── potions/              # Potion data by rarity
```

## Usage

### Generating Magic Items
1. Navigate to the **Magic Item Generator** tab
2. Select a character (or leave as default)
3. Optionally choose a specific table (A-K) or leave empty for random
4. Click "Generate Magic Item"
5. Copy the Discord-formatted output or click the item link

### Generating Spell Scrolls
1. In the Magic Item Generator tab, find the **Spell Scroll Generator** section
2. Select a spell level (0-9) or leave empty for random
3. Click "Generate Spell Scroll"
4. The output includes spell name and scroll value in gold

### Creating Shop Inventories
1. Go to the **Shop Generator** tab
2. Click any shop type button:
   - Magic Items Shop (12 items)
   - Spell Scrolls Shop (4 scrolls)
   - Potion Shop (4 potions)
   - Basic Items Shop (10 items)
   - Combined Shop (4 mixed items)
3. Copy the formatted inventory for Discord

### Calculating Rewards
1. Switch to the **Gold & Price Calculator** tab
2. For gold drops:
   - Enter the Challenge Rating (CR)
   - Enter number of monsters
   - Click "Calculate Gold Drop"
3. For item pricing:
   - Select item rarity
   - Select item condition
   - Click "Calculate Item Price"

## Configuration

Edit `config/config.py` to customize:
- Number of items per shop type
- Price ranges by rarity
- Item enchantment settings
- Character names
- Gold drop ranges by CR

## Data Files

The application reads from CSV files in the `data/` directory:
- Item lists organized by rarity
- Spell lists organized by level (0-9)
- Potion lists organized by type
- URL mappings in `magic_items_data.txt` and `spell_data.txt`

### Adding Custom Items
1. Add items to the appropriate CSV file (one per line)
2. For items with URLs, add entries to `magic_items_data.txt`:
   ```
   Item Name[TAB]URL
   ```

## Discord Integration

All generated content is formatted for Discord with:
- **Bold** item names
- Emoji indicators for rarity
- Code blocks for structured data
- Clickable URLs in angle brackets `<URL>`
- Bot commands for items without URLs (`!item`)

## Tips

- Leave fields empty for random generation
- The reference table shows dice formulas for each rarity
- Generated prices vary within configured ranges
- Spell scroll prices are fixed by level
- Item conditions affect final selling price

## Credits

Created for D&D 5th Edition campaigns. Not affiliated with Wizards of the Coast.

## License

This project is provided as-is for personal use in tabletop gaming.