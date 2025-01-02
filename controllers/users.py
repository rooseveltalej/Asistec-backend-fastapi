import re
from fastapi import HTTPException
from db.mongo_client import mongo_client
from models.users import UserModel
from schemas.users import UserLogin
import bcrypt



db = mongo_client.get_database()


def hash_password(plain_password: str) -> str:
    """
    Genera un hash seguro para la contraseña usando bcrypt.
    """
    salt = bcrypt.gensalt()  # Genera una sal aleatoria
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con el hash.
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


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
        user_data["password"] = hash_password(user_data["password"])
        user = UserModel(**user_data)
        user_dict = user.dict()
        user_dict.pop("id", None)  # Si no existe, no lanza excepción
        result = await collection.insert_one(user_dict)
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
async def user_login_controller(login_data: UserLogin):
    """
    Verifica las credenciales del usuario y retorna su información básica.
    """
    email = login_data['email']
    password = login_data['password']

    if not email or not password:
        raise HTTPException(status_code=400, detail="Correo y contraseña son obligatorios")

    # Buscar el usuario en la base de datos
    collection = db["users"]
    user = await collection.find_one({"email": email})

    if not user:
        raise HTTPException(status_code=400, detail="El usuario no existe. Por favor crea una cuenta.")

    # Convertir ObjectId a string para que sea serializable
    user_id = str(user["_id"])

    # Verificar la contraseña
    if not verify_password(password, user["password"]):  # Validando con bcrypt
        raise HTTPException(status_code=403, detail="Contraseña incorrecta.")

    # Retornar solo los datos necesarios
    return {"userId": user_id, "name": user["name"]}