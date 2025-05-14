from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.contact import ContactInDB, ContactCreate, ContactUpdate
from app.services.contact_service import ContactService

router=APIRouter()

@router.post("/", response_model=ContactInDB)
async def create_contact_router(contact_in:ContactCreate,db:AsyncSession=Depends(get_db)):
    return await ContactService.create_contact(db,contact_in)

@router.get("/{contact_id}", response_model=ContactInDB)
async def get_contact_by_id_router(contact_id:int,db:AsyncSession=Depends(get_db)):
    contact= await ContactService.get_contact_by_id(db,contact_id)
    if not contact:
        raise HTTPException(status_code=404,detail= "Contact not found")
    return contact

@router.get("/", response_model=List[ContactInDB])
async def get_all_contacts_router(db:AsyncSession=Depends(get_db)):
    return await ContactService.get_all_contacts(db)

@router.put("/{contact_id}", response_model=ContactInDB)
async def update_contact_router(contact_id: int, contact_in: ContactUpdate, db: AsyncSession = Depends(get_db)):
    updated_contact = await ContactService.update_contact(db, contact_id, contact_in)
    if not updated_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated_contact

@router.delete("/{contact_id}")
async def delete_contact_router(contact_id: int, db: AsyncSession = Depends(get_db)):
    deleted_contact = await ContactService.delete_contact(db, contact_id)
    if not deleted_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}
