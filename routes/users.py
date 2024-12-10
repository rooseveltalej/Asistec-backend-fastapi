from fastapi import APIRouter
from controllers.users import create_user, user_login_controller
from schemas.users import UserCreate, UserLogin, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user_endpoint(user_data: UserCreate):
    """
    Endpoint para crear un usuario.
    """
    return await create_user(user_data.dict())

@router.post("/login")
async def user_login_endpoint(login_data: UserLogin):
    """
    Endpoint para que un usuario inicie sesión.
    """
    return await user_login_controller(login_data.dict())
