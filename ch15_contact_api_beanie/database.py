import os

import motor.motor_asyncio
from beanie import init_beanie
from dotenv import load_dotenv

from models import Contact

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

async def init_db():
    client= motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
    await  init_beanie(database=client.get_default_database(),document_models=[Contact])