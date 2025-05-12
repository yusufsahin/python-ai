from typing import List

from fastapi import HTTPException

from models import Contact

async def create_contact(data: dict) -> Contact:
    contact = Contact(**data)
    return await contact.insert()

async def get_contact(contact_id: str) -> Contact:
    return await Contact.get(contact_id)

async def get_all_contacts() -> List[Contact]:
    return await Contact.find_all().to_list()

async def update_contact(contact_id: str, data: dict) -> Contact:
    contact = await Contact.get(contact_id)
    if not contact:
        raise HTTPException(status_code=404,detail="Contact not found")
    await contact.update({"$set": data})
    return await Contact.get(contact_id)

async def delete_contact(contact_id: str) -> bool:
    contact= await Contact.get(contact_id)
    if contact is None:
        return False
    await contact.delete()
    return True
