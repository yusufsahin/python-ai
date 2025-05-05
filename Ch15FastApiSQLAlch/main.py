from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import engine
from models import Base
@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
app=FastAPI(lifespan=lifespan)

from routes import router
app.include_router(router)
