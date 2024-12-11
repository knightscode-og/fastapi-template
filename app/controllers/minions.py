
from fastapi import HTTPException
from odmantic import ObjectId
from app.models.minions import Minions
from app.models.minion_types import MinionTypes
from app.core.logging import logger
from app.db.database import get_db

async def create_minion(minion: Minions):
    engine = get_db()
    """Create a new minion."""
    logger.info(f"Received request to create minion: {minion.type}")
    try:
        # Validate type_id reference
        minion_type = await engine.find_one(MinionTypes, MinionTypes.id == minion.type_id)
        if not minion_type:
            raise HTTPException(status_code=400, detail="Invalid minion type ID")
        
        await engine.save(minion)
        logger.info(f"Minion created successfully: {minion.type}")
        return minion
    except Exception as e:
        logger.error(f"Error creating minion: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def get_minion(minion_id: str):
    engine = get_db()
    """Get a minion by ID."""
    logger.info(f"Fetching minion with ID: {minion_id}")
    try:
        obj_id = ObjectId(minion_id)
        minion = await engine.find_one(Minions, Minions.id == obj_id)
        if not minion:
            logger.warning(f"Minion not found with ID: {minion_id}")
            raise HTTPException(status_code=404, detail="Minion not found")
        logger.info(f"Minion found: {minion.type}")
        return minion
    except Exception as e:
        logger.error(f"Error fetching minion with ID {minion_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")