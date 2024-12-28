from pydantic import BaseModel, Field
from bson import ObjectId
from pydantic.class_validators import root_validator

# Clase personalizada para manejar ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        """
        Define cómo se debe serializar a JSON en la documentación de Pydantic.
        """
        field_schema = handler(core_schema)
        field_schema.update(type="string")
        return field_schema

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        """
        Define cómo Pydantic debe manejar la validación y serialización.
        """
        from pydantic_core.core_schema import general_plain_validator_function
        return general_plain_validator_function(cls.validate)

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return ObjectId(value)


# Modelo de usuario
class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: str
    password: str
    name: str

    class Config:
        arbitrary_types_allowed = True  # Permitir tipos arbitrarios (como PyObjectId)
        json_encoders = {PyObjectId: str}  # Convertir ObjectId a string en JSON