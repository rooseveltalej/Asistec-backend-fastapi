from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        field_schema = handler(core_schema)
        field_schema.update(type="string")
        return field_schema

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        from pydantic_core.core_schema import general_plain_validator_function
        return general_plain_validator_function(cls.validate)

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)

    def __str__(self):
        return str(self)

class ActivityModel(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    idRelacion: int
    start: datetime
    end: datetime
    title: str
    description: str
    modalityType: str
    color: str
    type: str
    day: int
    userId: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
