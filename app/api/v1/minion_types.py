
from fastapi import APIRouter
from app.controllers.minion_types import create_minion_type, get_minion_type
from app.models.minion_types import MinionTypes

# Initialize router
router = APIRouter()

@router.post("/")
async def create_minion_type_route(minion_type: MinionTypes):
    return await create_minion_type(minion_type)

@router.get("/{minion_type_id}")
async def get_minion_type_route(minion_type_id: str):
    return await get_minion_type(minion_type_id)