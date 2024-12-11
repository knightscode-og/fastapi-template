from odmantic import AIOEngine
import motor.motor_asyncio
from app.core.logging import logger

# Global variables for the database connection
client = None
engine = None

async def init_db():
    """Initialize the MongoDB client and engine."""
    global client, engine
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb+srv://traveler_admin:vsbrfrKZqaT18PAA@cluster0.uvx7n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    engine = AIOEngine(client=client, database="traveler")
    logger.debug(f"Database engine initialized: {engine}")

async def close_db():
    """Close the MongoDB client."""
    global client
    if client:
        client.close()

def get_db():
    """Return the initialized database engine."""
    if engine is None:
        raise RuntimeError("Database engine is not initialized")
    return engine
