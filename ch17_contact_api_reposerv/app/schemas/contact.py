from typing import Optional

from pydantic import BaseModel, EmailStr


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email:EmailStr
    phone_number: Optional[str]=None
    address: Optional[str]=None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    email: Optional[EmailStr]=None
    phone_number: Optional[str]=None
    address: Optional[str]=None

class ContactInDB(ContactBase):
    id: int

    class Config:
        orm_mode = True