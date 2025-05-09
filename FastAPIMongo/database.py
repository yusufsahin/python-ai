import os
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
client=motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db=client.contact_db
collection=db.contacts