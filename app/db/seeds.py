import asyncio
from datetime import datetime
from app.db.database import init_db, get_db
from app.models.tame_types import TameTypes  # Import the TameTypes model

async def seed_tame_types():
    db = get_db()
    tame_types = [
        TameTypes(
            type="Dragon",
            min_health=100,
            max_health=200,
            min_attack=50,
            max_attack=100,
            ability="Fire Breath",
            created_at=datetime.utcnow(),
            updated_at=None
        ),
        TameTypes(
            type="Wolf",
            min_health=50,
            max_health=100,
            min_attack=20,
            max_attack=40,
            ability="Bite",
            created_at=datetime.utcnow(),
            updated_at=None
        ),
        TameTypes(
            type="Bear",
            min_health=150,
            max_health=300,
            min_attack=30,
            max_attack=60,
            ability="Swipe",
            created_at=datetime.utcnow(),
            updated_at=None
        ),
    ]
    await db.save_all(tame_types)

if __name__ == "__main__":
    asyncio.run(init_db())
    asyncio.run(seed_tame_types())
