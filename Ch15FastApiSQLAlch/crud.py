from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Contact
from schemas import ContactCreate, ContactUpdate


async def create_contact(db:AsyncSession, contact:ContactCreate):
    new_contact = Contact(**contact.model_dump())
    db.add(new_contact)
    await db.commit()
    await db.refresh(new_contact)
    return new_contact

async  def get_contact(db:AsyncSession,contact_id:int ):
    result = await db.execute(select(Contact).where(Contact.id == contact_id))
    return result.scalar_one_or_none()

async def get_all_contacts(db:AsyncSession):
    result = await db.execute(select(Contact))
    return result.scalars().all()

async def update_contact(db:AsyncSession, contact_id:int, contact:ContactUpdate):
    db_contact =await get_contact(db,contact_id)
    if not db_contact:
        return None
    for field,value in contact.model_dump().items():
        setattr(db_contact, field,value)
    await db.commit()
    await db.refresh(db_contact)
    return db_contact
async def delete_contact(db:AsyncSession, contact_id:int):
    db_contact = await get_contact(db,contact_id)
    if not db_contact:
        return None
    await db.delete(db_contact)
    await db.commit()
    return True