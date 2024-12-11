
from fastapi import HTTPException
from odmantic import ObjectId
from app.models.tame_types import TameTypes
from app.core.logging import logger
from app.db.database import get_db

async def create_tame_type(tame_type: TameTypes):
    engine = get_db()
    """Create a new tame type."""
    logger.info(f"Received request to create tame type: {tame_type.type}")
    try:
        await engine.save(tame_type)
        logger.info(f"Tame type created successfully: {tame_type.type}")
        return tame_type
    except Exception as e:
        logger.error(f"Error creating tame type: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def get_tame_type(tame_type_id: str):
    engine = get_db()
    """Get a tame type by ID."""
    logger.info(f"Fetching tame type with ID: {tame_type_id}")
    try:
        obj_id = ObjectId(tame_type_id)
        tame_type = await engine.find_one(TameTypes, TameTypes.id == obj_id)
        if not tame_type:
            logger.warning(f"Tame type not found with ID: {tame_type_id}")
            raise HTTPException(status_code=404, detail="Tame type not found")
        logger.info(f"Tame type found: {tame_type.type}")
        return tame_type
    except Exception as e:
        logger.error(f"Error fetching tame type with ID {tame_type_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")