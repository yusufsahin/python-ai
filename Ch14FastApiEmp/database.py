import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

print("🧪 DATABASE_URL:", DATABASE_URL)
async def get_connection():
    return await asyncpg.connect(DATABASE_URL)