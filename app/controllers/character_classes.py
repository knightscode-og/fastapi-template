
from fastapi import HTTPException
from odmantic import ObjectId
from app.models.character_classes import CharacterClasses
from datetime import datetime
from app.core.logging import logger
from app.db.database import get_db

async def create_character_class(character_class: CharacterClasses):
    engine = get_db()
    """Create a new character class."""
    logger.info(f"Received request to create character class: {character_class.name}")
    try:
        character_class.created_at = datetime.utcnow()
        character_class.updated_at = datetime.utcnow()
        await engine.save(character_class)
        logger.info(f"Character class created successfully: {character_class.name}")
        return character_class
    except Exception as e:
        logger.error(f"Error creating character class: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def get_character_class(character_class_id: str):
    engine = get_db()
    """Get a character class by ID."""
    logger.info(f"Fetching character class with ID: {character_class_id}")
    try:
        obj_id = ObjectId(character_class_id)
        character_class = await engine.find_one(CharacterClasses, CharacterClasses.id == obj_id)
        if not character_class:
            logger.warning(f"Character class not found with ID: {character_class_id}")
            raise HTTPException(status_code=404, detail="Character class not found")
        logger.info(f"Character class found: {character_class.name}")
        return character_class
    except Exception as e:
        logger.error(f"Error fetching character class with ID {character_class_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def update_character_class(character_class_id: str, updated_character_class: CharacterClasses):
    engine = get_db()
    """Update an existing character class by ID."""
    logger.info(f"Received request to update character class with ID: {character_class_id}")
    try:
        obj_id = ObjectId(character_class_id)
        character_class = await engine.find_one(CharacterClasses, CharacterClasses.id == obj_id)
        if not character_class:
            logger.warning(f"Character class not found with ID: {character_class_id}")
            raise HTTPException(status_code=404, detail="Character class not found")
        
        character_class.name = updated_character_class.name
        character_class.description = updated_character_class.description
        character_class.updated_at = datetime.utcnow()
        
        await engine.save(character_class)
        logger.info(f"Character class updated successfully: {character_class.name}")
        return character_class
    except Exception as e:
        logger.error(f"Error updating character class with ID {character_class_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")