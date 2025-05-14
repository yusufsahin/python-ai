from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.contact_repository import ContactRepository
from app.db.session import get_db
from app.schemas.contact import ContactInDB, ContactCreate
from app.services.contact_service import ContactService

router=APIRouter()

@router.post("/", response_model=ContactInDB)
async def create_contact_router(contact_in:ContactCreate,db:AsyncSession=Depends(get_db)):
    return await ContactService.create_contact(db,contact_in)