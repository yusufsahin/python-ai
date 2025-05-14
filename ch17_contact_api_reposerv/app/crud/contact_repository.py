from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactUpdate


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

    @staticmethod
    async def get_all(db:AsyncSession)-> list[Contact]:
        result = await db.execute(select(Contact))
        return result.scalars().all()

    @staticmethod
    async def update(db:AsyncSession,db_obj:Contact,contact_in:ContactUpdate)-> Contact:
        obj_data = contact_in.model_dump(exclude_unset=True)

        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    @staticmethod
    async def delete(db:AsyncSession,db_obj:Contact):
        await db.delete(db_obj)
        await db.commit()
        return db_obj