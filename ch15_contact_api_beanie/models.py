from beanie import Document
from pydantic import Field, EmailStr


class Contact(Document):
    full_name: str=Field(...,min_length=2,max_length=100)
    email:EmailStr
    phone:str=Field(...,min_length=10,max_length=20)

    class Settings:
        name="contacts"