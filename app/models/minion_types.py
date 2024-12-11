from odmantic import Model
from datetime import datetime
from typing import Optional

class MinionTypes(Model):
    type: str  # Unique identifier for the minion type
    min_health: int
    max_health: int
    min_attack: int
    max_attack: int
    created_at: datetime = datetime.utcnow()
    updated_at: Optional[datetime] = None
