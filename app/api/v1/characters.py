from fastapi import APIRouter
from app.controllers.characters import create_character, get_character, update_character, recruit_minion, tame_tame, update_battle_formation
from app.models.characters import Characters
from typing import List

# Initialize router
router = APIRouter()

@router.post("/")
async def create_character_route(character: Characters):
    return await create_character(character)

@router.get("/{character_id}")
async def get_character_route(character_id: str):
    return await get_character(character_id)

@router.put("/{character_id}")
async def update_character_route(character_id: str, updated_character: Characters):
    return await update_character(character_id, updated_character)

@router.post("/{character_id}/recruit/{minion_type_id}")
async def recruit_minion_route(character_id: str, minion_type_id: str):
    return await recruit_minion(character_id, minion_type_id)

@router.post("/{character_id}/tame/{tame_type_id}")
async def tame_tame_route(character_id: str, tame_type_id: str):
    return await tame_tame(character_id, tame_type_id)

@router.put("/{character_id}/update_battle_formation")
async def update_battle_formation_route(character_id: str, battle_formation: List[str]):
    return await update_battle_formation(character_id, battle_formation)
