from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.endpoints import contact

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    title="Contact API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(contact.router, prefix="/api/v1/contacts", tags=["contacts"])
