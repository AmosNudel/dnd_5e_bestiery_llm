import json
import os
import glob
from agents import function_tool

@function_tool
def read_spell_by_name(spell_name: str) -> str:
    """
    Search for spells by name across all school-specific spell files.
    Uses soft search (partial name matching).
    """
    spell_name_lower = spell_name.lower()
    found_spells = []
    
    # Search through all school-specific spell files
    spell_files = glob.glob("data/spells_by_school/spells_*.json")
    
    if not spell_files:
        return "No spell files found. Please run the spell organization script first."
    
    for file_path in spell_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                school_data = json.load(f)
                
            # Search through spells in this school
            for spell in school_data.get("spells", []):
                spell_name_in_file = spell.get("name", "").lower()
                if spell_name_lower in spell_name_in_file:
                    found_spells.append(spell)
                    
        except Exception as e:
            continue  # Skip files that can't be read
    
    if not found_spells:
        return "No spells found"
    
    # Return the raw JSON objects
    if len(found_spells) == 1:
        return json.dumps(found_spells[0], indent=2)
    else:
        return json.dumps(found_spells, indent=2)

@function_tool
def read_spell_by_school(school: str) -> str:
    """
    Search for all spells in a specific school of magic.
    """
    spell_files = glob.glob("data/spells_by_school/spells_*.json")
    schools = {
        "abjuration": "A",
        "conjuration": "C", 
        "divination": "D",
        "enchantment": "E",
        "evocation": "V",
        "illusion": "I",
        "necromancy": "N",
        "transmutation": "T",
    }
    
    school_code = schools.get(school.lower())
    if not school_code:
        return "Invalid school name. Use: abjuration, conjuration, divination, enchantment, evocation, illusion, necromancy, transmutation"
    
    found_spells = []
    
    for file_path in spell_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                school_data = json.load(f)
                for spell in school_data.get("spells", []):
                    if spell.get("school") == school_code:
                        found_spells.append(spell)
        except Exception as e:
            continue
    
    if not found_spells:
        return "No spells found in this school"
    
    return json.dumps(found_spells, indent=2)

@function_tool
def read_spell_by_level(level: int) -> str:
    """
    Search for all spells of a specific level.
    """
    spell_files = glob.glob("data/spells_by_school/spells_*.json")
    found_spells = []
    
    for file_path in spell_files:
        with open(file_path, "r", encoding="utf-8") as f:
            level_data = json.load(f)
            for spell in level_data.get("spells", []):
                if spell.get("level") == level:
                    found_spells.append(spell)
    return json.dumps(found_spells, indent=2)





