from models import ContactCreate, ContactOut, ContactUpdate
from database import  collection
from bson import ObjectId

def format_document(document:dict | None)-> dict | None:
    """ Convert MongoDb ObjectId to string for JSON serialization """
    if document and "_id" in document:
        document["_id"] = str(document["_id"])
    return document

async  def create_contact(data:ContactCreate) -> dict | None:
    """ Create a new contact """
    result= await collection.insert_one(data.model_dump())
    new_contact= await collection.find_one({"_id":result.inserted_id})
    return format_document(new_contact)

async def get_contact(contact_id:str) -> dict | None:
    """ Get a contact by id """
    contact= await collection.find_one({"_id":ObjectId(contact_id)})
    return format_document(contact)
async def get_all_contacts() -> list[dict]:
    """ Get all contacts """
    contacts= await collection.find().to_list(length=100)
    return [format_document(contact) for contact in contacts]

async def update_contact(contact_id: str, data: ContactUpdate) -> dict | None:
    """Update a contact by ID and return the updated document."""
    await collection.update_one(
        {"_id": ObjectId(contact_id)},
        {"$set": data.model_dump(exclude_unset=True)}
    )
    return await get_contact(contact_id)


async def delete_contact(contact_id:str) -> bool:
    """ Delete a contact by id """
    result= await collection.delete_one({"_id":ObjectId(contact_id)})
    return result.deleted_count==1