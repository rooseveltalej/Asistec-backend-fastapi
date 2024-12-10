from pydantic import BaseModel, EmailStr

# Esquema para crear un usuario
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str

# Esquema para iniciar sesión
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Esquema para la respuesta del usuario
class UserResponse(BaseModel):
    email: EmailStr
    name: str
