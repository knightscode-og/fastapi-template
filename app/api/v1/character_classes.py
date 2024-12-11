
from fastapi import APIRouter
from app.controllers.character_classes import create_character_class, get_character_class, update_character_class
from app.models.character_classes import CharacterClasses

# Initialize router
router = APIRouter()

@router.post("/")
async def create_character_class_route(character_class: CharacterClasses):
    return await create_character_class(character_class)

@router.get("/{character_class_id}")
async def get_character_class_route(character_class_id: str):
    return await get_character_class(character_class_id)

@router.put("/{character_class_id}")
async def update_character_class_route(character_class_id: str, updated_character_class: CharacterClasses):
    return await update_character_class(character_class_id, updated_character_class)