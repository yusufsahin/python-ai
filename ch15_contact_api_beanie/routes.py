from fastapi import APIRouter, HTTPException

from crud import create_contact, get_all_contacts, get_contact, update_contact, delete_contact
from models import Contact

router =APIRouter(prefix="/api/contacts", tags=["Contacts"])

@router.post("/",response_model=Contact)
async  def create(data:dict):
    return  await create_contact(data)

@router.get("/",response_model=list[Contact])
async def get_all():
    return await get_all_contacts()

@router.get("/{contact_id}",response_model=Contact)
async def get(contact_id:str):
    contact= await get_contact(contact_id)
    if contact:
        return contact
    raise HTTPException(status_code=404, detail="Contact not found")

@router.put("/{contact_id}",response_model=Contact)
async def update(contact_id:str,data:dict):
    contact= await get_contact(contact_id)
    if contact:
        return await update_contact(contact_id,data)
    raise HTTPException(status_code=404, detail="Contact not found")

@router.delete("/{contact_id}", response_model=bool, status_code=200)
async def delete(contact_id: str):
    deleted = await delete_contact(contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return True