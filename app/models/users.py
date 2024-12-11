from odmantic import Model, Field
from datetime import datetime

class Users(Model):
    username: str
    email: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
