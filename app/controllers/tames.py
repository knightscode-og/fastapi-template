from fastapi import HTTPException
from odmantic import ObjectId
from app.models.tames import Tames
from app.models.tame_types import TameTypes
from app.core.logging import logger
from app.db.database import get_db

async def create_tame(tame: Tames):
    engine = get_db()
    """Create a new tame."""
    logger.info(f"Received request to create tame: {tame.type}")
    try:
        # Validate type_id reference
        tame_type = await engine.find_one(TameTypes, TameTypes.id == tame.type_id)
        if not tame_type:
            raise HTTPException(status_code=400, detail="Invalid tame type ID")
        
        await engine.save(tame)
        logger.info(f"Tame created successfully: {tame.type}")
        return tame
    except Exception as e:
        logger.error(f"Error creating tame: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def get_tame(tame_id: str):
    engine = get_db()
    """Get a tame by ID."""
    logger.info(f"Fetching tame with ID: {tame_id}")
    try:
        obj_id = ObjectId(tame_id)
        tame = await engine.find_one(Tames, Tames.id == obj_id)
        if not tame:
            logger.warning(f"Tame not found with ID: {tame_id}")
            raise HTTPException(status_code=404, detail="Tame not found")
        logger.info(f"Tame found: {tame.type}")
        return tame
    except Exception as e:
        logger.error(f"Error fetching tame with ID {tame_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")