
from fastapi import APIRouter
from app.controllers.minions import create_minion, get_minion
from app.models.minions import Minions

# Initialize router
router = APIRouter()

@router.post("/")
async def create_minion_route(minion: Minions):
    return await create_minion(minion)

@router.get("/{minion_id}")
async def get_minion_route(minion_id: str):
    return await get_minion(minion_id)