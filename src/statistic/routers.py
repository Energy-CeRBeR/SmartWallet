from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.card_operations.models import card, type_card
from src.auth.base_config import current_user
from src.transactions.schemas import CreateInCategory, CreateExCategory, CreateIncome, CreateExpense
from src.transactions.models import in_category, ex_category, income, expense

router = APIRouter(
    prefix="/statistic",
    tags=["statistic"],
    dependencies=[Depends(current_user)]
)


@router.get("/balance/")
async def get_total_balance(user=Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    card_balances = await session.execute(select(card.c.balance).
                                          where((card.c.type_id != 2) & (card.c.user_id == user.id)))
    total_balance = 0
    for elem in card_balances.mappings().all():
        total_balance += elem["balance"]

    return {"Общий баланс": str(total_balance)}


@router.get("/incomes_by_category/")
async def get_incomes_by_category(category_id: int, user=Depends(current_user),
                                  session: AsyncSession = Depends(get_async_session)):
    card_id = (await session.execute(select(income.c.card_id).where(income.c.category_id == category_id))).scalar()
    user_id = (await session.execute(select(card.c.user_id).where(card.c.id == card_id))).scalar()
    if user_id == user.id:
        income_amounts = await session.execute(select(income.c.amount).where((income.c.category_id == category_id)))
        total_income = 0
        for elem in income_amounts.mappings().all():
            total_income += elem["amount"]
        return {"Доходы по данной категории": str(total_income)}
    else:
        return {"status": "Отказано в доступе"}


@router.get("/expenses_by_category/")
async def get_expenses_by_category(category_id: int, user=Depends(current_user),
                                   session: AsyncSession = Depends(get_async_session)):
    card_id = (await session.execute(select(expense.c.card_id).where(expense.c.category_id == category_id))).scalar()
    user_id = (await session.execute(select(card.c.user_id).where(card.c.id == card_id))).scalar()
    if user_id == user.id:
        expense_amounts = await session.execute(select(expense.c.amount).where((expense.c.category_id == category_id)))
        total_expense = 0
        for elem in expense_amounts.mappings().all():
            total_expense += elem["amount"]
        return {"Расходы по данной категории": str(total_expense)}
    else:
        return {"status": "Отказано в доступе"}


@router.get("/all_incomes")
async def get_all_incomes(user=Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    card_id_tuple = list(map(lambda x: int(x[0]), (await session.execute(select(card.c.id).
                                                                         where((card.c.user_id == user.id)
                                                                               & (card.c.type_id == 1)))).all()))
    income_amounts = await session.execute(select(income.c.amount).where(income.c.card_id.in_(card_id_tuple)))
    total_income = 0
    for elem in income_amounts.mappings().all():
        total_income += elem["amount"]

    return {"Общая сумма доходов": str(total_income)}


@router.get("/all_expenses")
async def get_all_expenses(user=Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    card_id_tuple = list(map(lambda x: int(x[0]), (await session.execute(select(card.c.id).
                                                                         where((card.c.user_id == user.id)
                                                                               & (card.c.type_id == 1)))).all()))
    expense_amounts = await session.execute(select(expense.c.amount).where(expense.c.card_id.in_(card_id_tuple)))
    total_expense = 0
    for elem in expense_amounts.mappings().all():
        total_expense += elem["amount"]

    return {"Общая сумма расходов": str(total_expense)}
