
from fastapi import HTTPException
from odmantic import ObjectId
from app.models.minion_types import MinionTypes
from app.core.logging import logger
from app.db.database import get_db

async def create_minion_type(minion_type: MinionTypes):
    engine = get_db()
    """Create a new minion type."""
    logger.info(f"Received request to create minion type: {minion_type.type}")
    try:
        await engine.save(minion_type)
        logger.info(f"Minion type created successfully: {minion_type.type}")
        return minion_type
    except Exception as e:
        logger.error(f"Error creating minion type: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def get_minion_type(minion_type_id: str):
    engine = get_db()
    """Get a minion type by ID."""
    logger.info(f"Fetching minion type with ID: {minion_type_id}")
    try:
        obj_id = ObjectId(minion_type_id)
        minion_type = await engine.find_one(MinionTypes, MinionTypes.id == obj_id)
        if not minion_type:
            logger.warning(f"Minion type not found with ID: {minion_type_id}")
            raise HTTPException(status_code=404, detail="Minion type not found")
        logger.info(f"Minion type found: {minion_type.type}")
        return minion_type
    except Exception as e:
        logger.error(f"Error fetching minion type with ID {minion_type_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")