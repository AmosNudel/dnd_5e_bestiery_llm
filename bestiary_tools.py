import glob
import json
from agents import function_tool

@function_tool
def read_bestiary_by_name(creature_name: str) -> str:
    """
    Read the bestiary for a given creature name across all monster types.
    Returns all matching creatures.
    """
    # Get all JSON files in the monsters_by_type directory
    print(f"Searching for {creature_name} in all monster types...")
    monster_files = glob.glob("data/monsters_by_type/*.json")
    matching_creatures = []
    
    for file_path in monster_files:
        try:
            with open(file_path, "r") as f:
                bestiary = json.load(f)
            
            # Search through the monsters array for the creature
            for monster in bestiary.get("monsters", []):
                if creature_name.lower() in monster.get("name", "").lower():
                    matching_creatures.append(monster)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
    
    if matching_creatures:
        return json.dumps(matching_creatures, indent=2)
    else:
        return "Creature not found"

@function_tool
def read_bestiary_by_cr(cr: str) -> str:
    """
    Read the bestiary for creatures with a given CR across all monster types.
    """
    # Get all JSON files in the monsters_by_type directory
    print(f"Searching for CR {cr} in all monster types...")
    monster_files = glob.glob("data/monsters_by_type/*.json")
    matching_creatures = []
    
    for file_path in monster_files:
        try:
            with open(file_path, "r") as f:
                bestiary = json.load(f)
            
            # Search through the monsters array for creatures with matching CR
            for monster in bestiary.get("monsters", []):
                if monster.get("cr") == cr:
                    matching_creatures.append(monster)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
    
    if matching_creatures:
        return json.dumps(matching_creatures, indent=2)
    else:
        return f"No creatures found with CR {cr}"

@function_tool
def read_bestiary_by_type(monster_type: str) -> str:
    """
    Read the bestiary for all creatures of a given type (beast, dragon, etc.).
    """
    print(f"Searching for {monster_type} in all monster types...")
    file_path = f"data/monsters_by_type/{monster_type.lower()}.json"
    
    try:
        with open(file_path, "r") as f:
            bestiary = json.load(f)
        
        return json.dumps(bestiary.get("monsters", []), indent=2)
    except FileNotFoundError:
        return f"Monster type '{monster_type}' not found"
    except Exception as e:
        return f"Error reading {file_path}: {e}"

@function_tool
def read_bestiary_by_size(size: str) -> str:
    """
    Read the bestiary for all creatures of a given size across all monster types.
    Size can be: T (tiny), S (small), M (medium), L (large), H (huge), G (gargantuan)
    """
    print(f"Searching for {size} in all monster types...")
    # Size mapping
    size_mapping = {
        "T": "tiny",
        "S": "small", 
        "M": "medium",
        "L": "large",
        "H": "huge",
        "G": "gargantuan"
    }
    
    # Normalize the size input
    size_upper = size.upper()
    if size_upper not in size_mapping:
        return f"Invalid size '{size}'. Valid sizes are: {', '.join(size_mapping.keys())}"
    
    # Get all JSON files in the monsters_by_type directory
    monster_files = glob.glob("data/monsters_by_type/*.json")
    matching_creatures = []
    
    for file_path in monster_files:
        try:
            with open(file_path, "r") as f:
                bestiary = json.load(f)
            
            # Search through the monsters array for creatures with matching size
            for monster in bestiary.get("monsters", []):
                monster_size = monster.get("size", [])
                if isinstance(monster_size, list) and size_upper in monster_size:
                    matching_creatures.append(monster)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
    
    if matching_creatures:
        return json.dumps(matching_creatures, indent=2)
    else:
        return f"No creatures found with size {size_upper} ({size_mapping[size_upper]})"
    
@function_tool
def read_bestiary_by_environment(environment: str) -> str:
    """
    Read the bestiary for all creatures of a given environment (forest, desert, etc.).
    """
    print(f"Searching for {environment} in all monster types...")
    # Get all JSON files in the monsters_by_type directory
    monster_files = glob.glob("data/monsters_by_type/*.json")
    matching_creatures = []
    
    for file_path in monster_files:
        try:
            with open(file_path, "r") as f:
                bestiary = json.load(f)
            
            # Search through the monsters array for creatures with matching environment
            for monster in bestiary.get("monsters", []):
                monster_environments = monster.get("environment", [])
                if isinstance(monster_environments, list) and environment.lower() in [env.lower() for env in monster_environments]:
                    matching_creatures.append(monster)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
    
    if matching_creatures:
        return json.dumps(matching_creatures, indent=2)
    else:
        return f"No creatures found in environment '{environment}'"
    
@function_tool
def read_monster_fluff(creature_name: str) -> str:
    """
    Read the fluff/lore information for a given creature name.
    """
    try:
        with open("data/fluff-bestiary-xmm.json", "r") as f:
            fluff_data = json.load(f)
        
        # Search through the monsterFluff array for the creature
        for monster_fluff in fluff_data.get("monsterFluff", []):
            if monster_fluff.get("name", "").lower() == creature_name.lower():
                return json.dumps(monster_fluff, indent=2)
        
        return f"Fluff information not found for {creature_name}"
    except FileNotFoundError:
        return "Fluff data file not found"
    except Exception as e:
        return f"Error reading fluff data: {e}"

