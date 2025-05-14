from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.contact_repository import ContactRepository
from app.schemas.contact import ContactCreate, ContactUpdate


class ContactService:
    @staticmethod
    async def create_contact(db:AsyncSession,contact_in:ContactCreate):
        return await ContactRepository.create(db,contact_in)

    @staticmethod
    async def get_contact_by_id(db:AsyncSession,contact_id:int):
        return await ContactRepository.get_by_id(db,contact_id)

    @staticmethod
    async def get_all_contacts(db:AsyncSession):
        return await ContactRepository.get_all(db)

    @staticmethod
    async def update_contact(db:AsyncSession,contact_id:int,contact_in:ContactUpdate):
        db_obj = await ContactRepository.get_by_id(db,contact_id)
        if not db_obj:
            return None
        return await ContactRepository.update(db,db_obj,contact_in)

    @staticmethod
    async def delete_contact(db:AsyncSession,contact_id:int):
        db_obj = await ContactRepository.get_by_id(db,contact_id)
        if not db_obj:
            return None
        return await ContactRepository.delete(db,db_obj)