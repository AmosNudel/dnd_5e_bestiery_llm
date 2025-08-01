# DM Assistant v2

A Dungeon Master's assistant powered by AI that can search through D&D 5e bestiary data to help with creature selection and monster information.

## Features

- **Creature Search by Name**: Find creatures by partial name matching
- **Search by Challenge Rating (CR)**: Find all creatures of a specific CR
- **Search by Monster Type**: Find all creatures of a specific type (beast, dragon, undead, etc.)
- **Search by Size**: Find creatures by size (Tiny, Small, Medium, Large, Huge, Gargantuan)
- **Search by Environment**: Find creatures that inhabit specific environments (arctic, desert, forest, etc.)

## Project Structure

```
dm_assistant_v2/
├── app.py                 # Main application with search functions
├── model.py              # AI agent configuration
├── requirements.txt      # Python dependencies
├── data/
│   ├── bestiary-xmm.json           # Complete bestiary data
│   └── monsters_by_type/           # Bestiary organized by monster type
│       ├── aberration.json
│       ├── beast.json
│       ├── celestial.json
│       ├── construct.json
│       ├── dragon.json
│       ├── elemental.json
│       ├── fey.json
│       ├── fiend.json
│       ├── giant.json
│       ├── humanoid.json
│       ├── monstrosity.json
│       ├── ooze.json
│       ├── plant.json
│       └── undead.json
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

The application will start an AI agent that can answer questions about creatures and help with encounter planning.

### Example Queries

You can ask the AI agent questions like:

- "Show me all CR 5 creatures"
- "Find all dragons"
- "What creatures live in the desert?"
- "Show me all large beasts"
- "Find creatures with 'goblin' in the name"
- "Which has higher ac, a fire giant or young red dragon?"
