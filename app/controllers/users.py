from fastapi import HTTPException
from odmantic import ObjectId
from app.models.users import Users
from datetime import datetime
from app.core.logging import logger
from app.db.database import get_db

async def create_user(user: Users):
    engine = get_db()
    """Create a new user."""
    logger.info(f"Received request to create user: {user.username}")
    try:
        user.created_at = datetime.utcnow()
        user.updated_at = datetime.utcnow()
        await engine.save(user)
        logger.info(f"User created successfully: {user.username}")
        return user
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def get_user(user_id: str):
    engine = get_db()
    """Get a user by ID."""
    logger.info(f"Fetching user with ID: {user_id}")
    try:
        obj_id = ObjectId(user_id)
        user = await engine.find_one(Users, Users.id == obj_id)
        if not user:
            logger.warning(f"User not found with ID: {user_id}")
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"User found: {user.username}")
        return user
    except Exception as e:
        logger.error(f"Error fetching user with ID {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def update_user(user_id: str, updated_user: Users):
    engine = get_db()
    """Update an existing user by ID."""
    logger.info(f"Received request to update user with ID: {user_id}")
    try:
        obj_id = ObjectId(user_id)
        user = await engine.find_one(Users, Users.id == obj_id)
        if not user:
            logger.warning(f"User not found with ID: {user_id}")
            raise HTTPException(status_code=404, detail="User not found")
        
        user.username = updated_user.username
        user.email = updated_user.email
        user.updated_at = datetime.utcnow()
        
        await engine.save(user)
        logger.info(f"User updated successfully: {user.username}")
        return user
    except Exception as e:
        logger.error(f"Error updating user with ID {user_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")