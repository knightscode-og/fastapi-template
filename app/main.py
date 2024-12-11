from fastapi import FastAPI
from app.api.v1 import users
from odmantic import AIOEngine
import motor.motor_asyncio
from app.core.logging import logger
from app.db.database import init_db, close_db

# Initialize FastAPI
app = FastAPI()

# Add the users and characters routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])


@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")
    await init_db()
    logger.info("Database initialized")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")
    await close_db()
    logger.info("Database connection closed")
