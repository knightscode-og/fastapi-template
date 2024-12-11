from fastapi import APIRouter
from app.controllers.users import create_user, get_user, update_user
from app.models.users import Users

# Initialize router
router = APIRouter()

@router.post("/")
async def create_user_route(user: Users):
    return await create_user(user)

@router.get("/{user_id}")
async def get_user_route(user_id: str):
    return await get_user(user_id)

@router.put("/{user_id}")
async def update_user_route(user_id: str, updated_user: Users):
    return await update_user(user_id, updated_user)