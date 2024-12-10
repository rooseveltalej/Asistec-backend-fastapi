from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId

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

    def __str__(self):
        return str(self)

# Modelo de usuario
class UserModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)  # Permitir tipos arbitrarios

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: str
    password: str
    name: str

    def dict(self, **kwargs):
        """
        Convierte el modelo a un diccionario, excluyendo el alias '_id' si no es necesario.
        """
        return super().dict(by_alias=True, exclude_none=True)
