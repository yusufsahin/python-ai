from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from crud import create_contact, get_all_contacts, get_contact, update_contact, delete_contact
from database import SessionLocal
from schemas import ContactOut, ContactCreate, ContactUpdate

router = APIRouter(prefix="/api/contacts",tags=['contacts'])

async def get_db():
    async with SessionLocal() as session:
        yield session


@router.post("/",response_model=ContactOut)
async def create(contact:ContactCreate,db:AsyncSession = Depends(get_db)):
    return await create_contact(db,contact)

@router.get("/",response_model=list[ContactOut])
async def list_all(db:AsyncSession = Depends(get_db)):
    return await get_all_contacts(db)

@router.get("/{contact_id}",response_model=ContactOut)
async def read (contact_id:int,db:AsyncSession = Depends(get_db)):
    result= await get_contact(db,contact_id)
    if not result:
        raise HTTPException(status_code=404,detail="Contact not found")
    return result

@router.put("/{contact_id}",response_model=ContactOut)
async def update(contact_id:int,contact:ContactUpdate,db:AsyncSession = Depends(get_db)):
    result= await update_contact(db,contact_id,contact)
    if not result:
        raise HTTPException(status_code=404,detail="Contact not found")
    return result
@router.delete("/{contact_id}")
async def delete(contact_id:int,db:AsyncSession = Depends(get_db)):
    if not await delete_contact(db,contact_id):
        raise HTTPException(status_code=404,detail="Contact not found")
    return {"detailed":"Deleted"}