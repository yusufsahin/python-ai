from fastapi import APIRouter, HTTPException

from crud import create_contact, get_all_contacts, get_contact, update_contact, delete_contact
from models import ContactOut, ContactCreate, ContactUpdate

router=APIRouter(prefix="/api/contacts", tags=["Contacts"])

@router.post("/", response_model=ContactOut)
async def create(contact: ContactCreate):
    return await create_contact(contact)

@router.get("/", response_model=list[ContactOut])
async def get_all():
    return await get_all_contacts()

@router.get("/{contact_id}", response_model=ContactOut)
async def read(contact_id: str):
    result = await get_contact(contact_id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@router.put("/{contact_id}", response_model=ContactOut)
async def update(contact_id: str, contact: ContactUpdate):
    result = await update_contact(contact_id, contact)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

@router.delete("/{contact_id}")
async  def delete(contact_id: str):
    if not await delete_contact(contact_id):
        raise HTTPException(status_code=404, detail="Not found")
    return {"detailed": "Deleted"}