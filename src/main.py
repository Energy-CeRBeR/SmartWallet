from fastapi_users import FastAPIUsers

from fastapi import FastAPI

from src.auth.base_config import auth_backend
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate


app = FastAPI(
    title="Shoe Store"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()