
from fastapi import APIRouter
from app.controllers.tame_types import create_tame_type, get_tame_type
from app.models.tame_types import TameTypes

# Initialize router
router = APIRouter()

@router.post("/")
async def create_tame_type_route(tame_type: TameTypes):
    return await create_tame_type(tame_type)

@router.get("/{tame_type_id}")
async def get_tame_type_route(tame_type_id: str):
    return await get_tame_type(tame_type_id)