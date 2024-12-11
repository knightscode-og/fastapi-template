from fastapi import APIRouter
from app.controllers.tames import create_tame, get_tame
from app.models.tames import Tames

# Initialize router
router = APIRouter()

@router.post("/")
async def create_tame_route(tame: Tames):
    return await create_tame(tame)

@router.get("/{tame_id}")
async def get_tame_route(tame_id: str):
    return await get_tame(tame_id)