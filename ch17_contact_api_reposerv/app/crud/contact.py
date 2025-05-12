from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.contact import Contact
from app.schemas.contact import ContactCreate


class ContactRepository:
    @staticmethod
    async def create(db:AsyncSession,contact_in:ContactCreate)-> Contact:
        contact = Contact(**contact_in.model_dump())
        db.add(contact)
        await db.commit()
        await db.refresh(contact)
        return contact

    @staticmethod
    async def get_by_id(db:AsyncSession,contact_id:int)-> Contact | None:
        result = await db.execute(select(Contact).where(Contact.id == contact_id))
        return result.scalar_one_or_none()