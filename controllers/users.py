import re
from fastapi import HTTPException
from db.mongo_client import mongo_client
from models.users import UserModel


db = mongo_client.get_database()

def hash_password(password: str) -> str:
    """
    Hashea la contraseña del usuario.
    TODO: Implementar un algoritmo de hash seguro.
    """
    return password


# Función para validar correos electrónicos
def validate_email(email: str) -> bool:
    """
    Valida que el correo tenga el dominio '@estudiantec.cr'
    """
    regex = r"^[a-zA-Z0-9._%+-]+@estudiantec\.cr$"
    return bool(re.match(regex, email))

# Controlador para crear un usuario
async def create_user(user_data: dict):
    """
    Crea un nuevo usuario si no existe y valida el correo.
    """
    email = user_data.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="El correo es obligatorio")

    # Validar que el correo tiene el formato correcto
    if not validate_email(email):
        raise HTTPException(
            status_code=400,
            detail="El correo debe ser de la forma '@estudiantec.cr'",
        )

    # Verificar si el usuario ya existe
    collection = db["users"]
    existing_user = await collection.find_one({"email": email})
    if existing_user:
        raise HTTPException(
            status_code=400, detail="El usuario ya existe. Por favor ingresa otro correo"
        )

    try:
        # Crear el usuario
        user = UserModel(**user_data)
        result = await collection.insert_one(user.dict())  # Pydantic manejará la conversión
        if not result.acknowledged:
            raise HTTPException(status_code=500, detail="Error al crear el usuario")
        return {
            "message": "Usuario creado correctamente",
            "id": str(result.inserted_id),
            "email": user.email,
            "name": user.name
        }
    except Exception as error:
        print("create_user_controller error:", error)
        raise HTTPException(status_code=500, detail="Error al crear el usuario")

# Controlador para iniciar sesión
async def user_login_controller(login_data: dict):
    """
    Verifica las credenciales del usuario.
    """
    email = login_data.get("email")
    password = login_data.get("password")
    # TODO hace falta decifrar la contraseña

    if not email or not password:
        raise HTTPException(status_code=400, detail="Correo y contraseña son obligatorios")

    # Buscar el usuario en la base de datos
    collection = db["users"]
    user = await collection.find_one({"email": email})
    if not user:
        raise HTTPException(
            status_code=400, detail="El usuario no existe. Por favor crea una cuenta"
        )

    # Verificar la contraseña
    user_model = UserModel(**user)
    if user_model.verify_password(password):
        return {"userId": str(user["_id"]), "name": user.get("name")}
    else:
        raise HTTPException(status_code=403, detail="La contraseña ingresada es incorrecta")
