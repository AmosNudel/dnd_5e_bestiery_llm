from pydantic import BaseModel
from typing import Dict, List

class Monster(BaseModel):
    name: str
    type: Dict[str]
    size: str
    alignment: str
    ac: int
    hp: str
    speed: Dict[str]
    cr: str
    source: str

    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    skill: Dict[str]
    save: Dict[str]
    languages: List[str]
    action: Dict[str]
    spellcasting: Dict[str]
    trait: Dict[str]
    legendary: Dict[str]
    environment: List[str]