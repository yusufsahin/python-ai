from pydantic import  BaseModel ,EmailStr,Field

class ContactBase(BaseModel):
    full_name: str=Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone:str=Field(..., min_length=10, max_length=20)

class ContactCreate(ContactBase):
    pass
class ContactUpdate(ContactBase):
    pass
class ContactOut(ContactBase):
    id: int

    class Config:
        from_attribute = True

