
from odmantic import Model
from datetime import datetime
from typing import Optional

class CharacterClasses(Model):
    name: str
    description: Optional[str] = None
    created_at: datetime = datetime.utcnow()
    updated_at: Optional[datetime] = None