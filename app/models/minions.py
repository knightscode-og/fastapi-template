from odmantic import Model
from bson import ObjectId
from datetime import datetime
from typing import Optional

class Minions(Model):
    type_id: ObjectId
    type: str
    master: ObjectId
    health: int
    attack: int
    created_at: datetime = datetime.utcnow()
    updated_at: Optional[datetime] = None