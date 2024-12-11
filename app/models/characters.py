from odmantic import Model
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

class Characters(Model):
    name: str
    char_class: str
    level: int
    party: List[str]
    skills: List[str] = []
    items: List[str] = []
    battle_formation: List[ObjectId] = []
    created_at: datetime
    updated_at: Optional[datetime]
