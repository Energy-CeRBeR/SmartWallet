from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.card_operations.models import card, type_card
from src.transactions.schemas import CreateInCategory, CreateExCategory, CreateIncome, CreateExpense
from src.transactions.models import in_category, ex_category, income, expense

router = APIRouter(
    prefix="/statistic",
    tags=["statistic"]
)


@router.get("/balance/")
async def get_total_balance(user_id: int, session: AsyncSession = Depends(get_async_session)):
    card_balances = await session.execute(select(card.c.balance).where(card.c.type_id != 2 and card.c.user_id == user_id))

    total_balance = 0
    for elem in card_balances.mappings().all():     # Попробовать усовершенствовать
        total_balance += elem["balance"]

    return total_balance


