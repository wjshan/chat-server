from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from .config import settings

engine = AsyncIOMotorClient(
    host=settings.db.host,
    port=settings.db.port,
    username=settings.db.user,
    password=settings.db.password
)

async def get_db() -> AsyncIOMotorClient:
    return engine[settings.db.name]


ActiveDB = Depends(get_db)
