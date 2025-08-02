# DM Assistant v2

A Dungeon Master's assistant powered by AI that can search through D&D 5e bestiary and spellcasting data to help with creature selection, monster information, and spell queries.

## Features

### Bestiary Tools

- **Creature Search by Name**: Find creatures by partial name matching
- **Search by Challenge Rating (CR)**: Find all creatures of a specific CR
- **Search by Monster Type**: Find all creatures of a specific type (beast, dragon, undead, etc.)
- **Search by Size**: Find creatures by size (Tiny, Small, Medium, Large, Huge, Gargantuan)
- **Search by Environment**: Find creatures that inhabit specific environments (arctic, desert, forest, etc.)
- **Monster Fluff**: Get additional lore and description for creatures

### Spellcasting Tools

- **Spell Search by Name**: Find spells by partial name matching
- **Search by School**: Find all spells in a specific school of magic
- **Search by Level**: Find all spells of a specific level

## Project Structure

```
dm_assistant_v2/
├── app.py                 # Main application with AI agents
├── bestiary_tools.py      # Bestiary search functions
├── spellcasting_tools.py  # Spell search functions
├── requirements.txt       # Python dependencies
├── data/
│   ├── bestiary-xmm.json           # Complete bestiary data
│   ├── fluff-bestiary-xmm.json     # Monster lore and descriptions
│   ├── monsters_by_type/           # Bestiary organized by monster type
│   │   ├── aberration.json
│   │   ├── beast.json
│   │   ├── celestial.json
│   │   ├── construct.json
│   │   ├── dragon.json
│   │   ├── elemental.json
│   │   ├── fey.json
│   │   ├── fiend.json
│   │   ├── giant.json
│   │   ├── humanoid.json
│   │   ├── monstrosity.json
│   │   ├── ooze.json
│   │   ├── plant.json
│   │   └── undead.json
│   ├── spells-xphb.json            # Complete spell data
│   └── spells_by_school/           # Spells organized by school
│       ├── spells_a.json
│       ├── spells_c.json
│       ├── spells_d.json
│       ├── spells_e.json
│       ├── spells_i.json
│       ├── spells_n.json
│       ├── spells_t.json
│       └── spells_v.json
└── README.md            # This file
```

## Setup

### Installation

1. **Clone or download the project**

   ```bash
   git clone <repository-url>
   cd dm_assistant_v2
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

### Running the Application

```bash
python app.py
```

The application will start AI agents that can answer questions about creatures and spells.

### Example Queries

**Bestiary Queries:**

- "Show me all CR 5 creatures"
- "Find all dragons"
- "What creatures live in the desert?"
- "Show me all large beasts"
- "Find creatures with 'goblin' in the name"
- "Which has higher AC, a fire giant or young red dragon?"
- "Tell me about adult white dragons"

**Spellcasting Queries:**

- "Give me a complete list of all cantrips"
- "Show me all evocation spells"
- "Find all 3rd level spells"
- "What is the fireball spell?"
- "Show me all abjuration spells"
