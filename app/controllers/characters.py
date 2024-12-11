from fastapi import HTTPException
from odmantic import ObjectId
from app.models.characters import Characters
from app.models.minions import Minions
from app.models.minion_types import MinionTypes
from datetime import datetime
from app.core.logging import logger
from app.db.database import get_db
from app.models.character_classes import CharacterClasses
import random
from app.models.tames import Tames
from app.models.tame_types import TameTypes
from typing import List

async def create_character(character: Characters):
    engine = get_db()
    """Create a new character."""
    logger.info(f"Received request to create character: {character.name}")
    try:
        # Validate char_class reference
        char_class = await engine.find_one(CharacterClasses, CharacterClasses.id == character.char_class)
        if not char_class:
            raise HTTPException(status_code=400, detail="Invalid character class ID")
        
        character.created_at = datetime.utcnow()
        character.updated_at = datetime.utcnow()
        await engine.save(character)
        logger.info(f"Character created successfully: {character.name}")
        return character
    except Exception as e:
        logger.error(f"Error creating character: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def get_character(character_id: str):
    engine = get_db()
    """Get a character by ID."""
    logger.info(f"Fetching character with ID: {character_id}")
    try:
        obj_id = ObjectId(character_id)
        character = await engine.find_one(Characters, Characters.id == obj_id)
        if not character:
            logger.warning(f"Character not found with ID: {character_id}")
            raise HTTPException(status_code=404, detail="Character not found")
        logger.info(f"Character found: {character.name}")
        return character
    except Exception as e:
        logger.error(f"Error fetching character with ID {character_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def update_character(character_id: str, updated_character: Characters):
    engine = get_db()
    """Update an existing character by ID."""
    logger.info(f"Received request to update character with ID: {character_id}")
    try:
        obj_id = ObjectId(character_id)
        character = await engine.find_one(Characters, Characters.id == obj_id)
        if not character:
            logger.warning(f"Character not found with ID: {character_id}")
            raise HTTPException(status_code=404, detail="Character not found")
        
        # Validate char_class reference
        char_class = await engine.find_one(CharacterClasses, CharacterClasses.id == updated_character.char_class)
        if not char_class:
            raise HTTPException(status_code=400, detail="Invalid character class ID")
        
        character.name = updated_character.name
        character.char_class = updated_character.char_class
        character.level = updated_character.level
        character.minions = updated_character.minions
        character.skills = updated_character.skills
        character.items = updated_character.items
        character.updated_at = datetime.utcnow()
        
        await engine.save(character)
        logger.info(f"Character updated successfully: {character.name}")
        return character
    except Exception as e:
        logger.error(f"Error updating character with ID {character_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def recruit_minion(character_id: str, minion_type_id: str):
    engine = get_db()
    """Recruit a minion to a character."""
    logger.info(f"Received request to recruit minion type with ID: {minion_type_id} to character with ID: {character_id}")
    try:
        char_obj_id = ObjectId(character_id)
        minion_type_obj_id = ObjectId(minion_type_id)
        
        character = await engine.find_one(Characters, Characters.id == char_obj_id)
        if not character:
            logger.warning(f"Character not found with ID: {character_id}")
            raise HTTPException(status_code=404, detail="Character not found")
        
        minion_type = await engine.find_one(MinionTypes, MinionTypes.id == minion_type_obj_id)
        if not minion_type:
            logger.warning(f"Minion type not found with ID: {minion_type_id}")
            raise HTTPException(status_code=404, detail="Minion type not found")
        
        health = random.randint(minion_type.min_health, minion_type.max_health)
        attack = random.randint(minion_type.min_attack, minion_type.max_attack)
        
        minion = Minions(
            type_id=minion_type.id,
            type=minion_type.type,
            master=char_obj_id,
            health=health,
            attack=attack,
            created_at=datetime.utcnow(),
            updated_at=None
        )
        
        await engine.save(minion)
        
        character.party.append(minion.id)
        character.updated_at = datetime.utcnow()
        
        await engine.save(character)
        logger.info(f"Minion with ID: {minion.id} recruited to character with ID: {character_id}")
        return character
    except Exception as e:
        logger.error(f"Error recruiting minion type with ID {minion_type_id} to character with ID {character_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def tame_tame(character_id: str, tame_type_id: str):
    engine = get_db()
    """Tame a tame for a character."""
    logger.info(f"Received request to tame tame type with ID: {tame_type_id} to character with ID: {character_id}")
    try:
        char_obj_id = ObjectId(character_id)
        tame_type_obj_id = ObjectId(tame_type_id)
        
        character = await engine.find_one(Characters, Characters.id == char_obj_id)
        if not character:
            logger.warning(f"Character not found with ID: {character_id}")
            raise HTTPException(status_code=404, detail="Character not found")
        
        tame_type = await engine.find_one(TameTypes, TameTypes.id == tame_type_obj_id)
        if not tame_type:
            logger.warning(f"Tame type not found with ID: {tame_type_id}")
            raise HTTPException(status_code=404, detail="Tame type not found")
        
        health = random.randint(tame_type.min_health, tame_type.max_health)
        attack = random.randint(tame_type.min_attack, tame_type.max_attack)
        
        tame = Tames(
            type_id=tame_type.id,
            type=tame_type.type,
            master=char_obj_id,
            health=health,
            attack=attack,
            created_at=datetime.utcnow(),
            updated_at=None
        )
        
        await engine.save(tame)
        
        character.party.append(tame.id)
        character.updated_at = datetime.utcnow()
        
        await engine.save(character)
        logger.info(f"Tame with ID: {tame.id} tamed to character with ID: {character_id}")
        return character
    except Exception as e:
        logger.error(f"Error taming tame type with ID {tame_type_id} to character with ID {character_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def update_battle_formation(character_id: str, battle_formation: List[str]):
    engine = get_db()
    """Update the battle formation of a character by ID."""
    logger.info(f"Received request to update battle formation for character with ID: {character_id}")
    try:
        obj_id = ObjectId(character_id)
        character = await engine.find_one(Characters, Characters.id == obj_id)
        if not character:
            logger.warning(f"Character not found with ID: {character_id}")
            raise HTTPException(status_code=404, detail="Character not found")
        
        max_formation_length = min(character.level + 1, 5)
        if len(battle_formation) > max_formation_length:
            raise HTTPException(status_code=400, detail=f"Battle formation length exceeds the allowed limit of {max_formation_length} for level {character.level}")
        character.battle_formation = [ObjectId(id) for id in battle_formation]
        character.updated_at = datetime.utcnow()
        
        await engine.save(character)
        logger.info(f"Battle formation updated successfully for character: {character.name}")
        return character
    except Exception as e:
        logger.error(f"Error updating battle formation for character with ID {character_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")