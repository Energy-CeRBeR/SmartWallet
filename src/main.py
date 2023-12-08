from fastapi_users import FastAPIUsers

from fastapi import FastAPI

from src.auth.base_config import auth_backend
from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate

from src.card_operations.routers import router as cards_router
from src.transactions.routers import router as transaction_router

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

app.include_router(cards_router)
app.include_router(transaction_router)
