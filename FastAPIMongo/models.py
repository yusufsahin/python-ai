from pydantic import BaseModel, Field,EmailStr
from bson import ObjectId
from typing import Any
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(cls.validate, core_schema.str_schema())

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        return {"type": "string"}
    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if isinstance(v, ObjectId):
            return v
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

class ContactBase(BaseModel):
    full_name: str=Field(...,min_length=2,max_length=100)
    email:EmailStr
    phone:str=Field(...,min_length=10,max_length=20)

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    pass

class ContactOut(ContactBase):
    id:PyObjectId=Field(alias="_id")
    class Config:
        populate_by_name = True
        json_encoders = {
            ObjectId: str
        }
        from_attributes = True