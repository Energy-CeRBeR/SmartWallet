from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.card_operations.models import card
from src.transactions.schemas import (CreateInCategory, CreateExCategory, CreateIncome, CreateExpense,
                                      UpdateIncome, UpdateExpense)
from src.transactions.models import in_category, ex_category, income, expense
from src.auth.base_config import current_user

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
    dependencies=[Depends(current_user)]
)


@router.get("/in_categories/")
async def get_in_category(user=Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(in_category).where(in_category.c.user_id == user.id)
    result = await session.execute(query)

    return result.mappings().all()


@router.get("/ex_categories/")
async def get_ex_category(user=Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(ex_category).where(ex_category.c.user_id == user.id)
    result = await session.execute(query)

    return result.mappings().all()


@router.post("/in_categories/")
async def add_in_category(new_in_category: CreateInCategory, user=Depends(current_user),
                          session: AsyncSession = Depends(get_async_session)):
    new_in_category = new_in_category.dict()
    new_in_category["user_id"] = user.id
    stmt = insert(in_category).values(**new_in_category)
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.post("/ex_categories/")
async def add_ex_category(new_ex_category: CreateExCategory, user=Depends(current_user),
                          session: AsyncSession = Depends(get_async_session)):
    new_ex_category = new_ex_category.dict()
    new_ex_category["user_id"] = user.id
    stmt = insert(ex_category).values(**new_ex_category)
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.delete("/in_categories/")
async def del_in_category(category_id: int, user=Depends(current_user),
                          session: AsyncSession = Depends(get_async_session)):
    to_delete = delete(in_category).where(in_category.c.id == category_id & in_category.c.user_id == user.id)
    await session.execute(to_delete)
    await session.commit()

    return {"status": "success"}


@router.delete("/ex_categories/")
async def del_ex_category(category_id: int, user=Depends(current_user),
                          session: AsyncSession = Depends(get_async_session)):
    to_delete = delete(ex_category).where(ex_category.c.id == category_id & ex_category.c.user_id == user.id)
    await session.execute(to_delete)
    await session.commit()

    return {"status": "success"}


@router.get("/incomes/")
async def get_income(card_id: int, user=Depends(current_user),
                     session: AsyncSession = Depends(get_async_session)):
    query = select(income).where(income.c.card_id == card_id & income.c.user_id == user.id)
    result = await session.execute(query)

    return result.mappings().all()


@router.get("/expenses/")
async def get_expense(card_id: int, user=Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    query = select(expense).where(expense.c.card_id == card_id & expense.c.user_id == user.id)
    result = await session.execute(query)

    return result.mappings().all()


@router.post("/incomes/")
async def add_income(new_income: CreateIncome, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(income).values(**new_income.dict())
    card_update = update(card).where(card.c.id == new_income.card_id).values(
        balance=card.c.balance + new_income.amount)
    await session.execute(stmt)
    await session.execute(card_update)
    await session.commit()

    return {"status": "success"}


@router.post("/expenses/")
async def add_expense(new_expense: CreateExpense, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(expense).values(**new_expense.dict())
    card_update = update(card).where(card.c.id == new_expense.card_id).values(
        balance=card.c.balance - new_expense.amount)
    await session.execute(stmt)
    await session.execute(card_update)
    await session.commit()

    return {"status": "success"}


@router.delete("/incomes/")
async def del_income(income_id: int, session: AsyncSession = Depends(get_async_session)):
    card_id = await session.execute(select(income.c.card_id).where(income.c.id == income_id))
    amount = await session.execute(select(income.c.amount).where(income.c.id == income_id))
    card_update = update(card).where(card.c.id == card_id.scalar()).values(
        balance=card.c.balance - amount.scalar())

    to_delete = delete(income).where(income.c.id == income_id)
    await session.execute(to_delete)
    await session.execute(card_update)
    await session.commit()

    return {"status": "success"}


@router.delete("/expenses/")
async def delete(expense_id: int, session: AsyncSession = Depends(get_async_session)):
    card_id = await session.execute(select(expense.c.card_id).where(expense.c.id == expense_id))
    amount = await session.execute(select(expense.c.amount).where(expense.c.id == expense_id))
    card_update = update(card).where(card.c.id == card_id.scalar()).values(
        balance=card.c.balance + amount.scalar())

    to_delete = delete(expense).where(expense.c.id == expense_id)
    await session.execute(to_delete)
    await session.execute(card_update)
    await session.commit()

    return {"status": "success"}


@router.put("/incomes/")
async def edit_income(current_income: UpdateIncome, session: AsyncSession = Depends(get_async_session)):
    new_version = update(income).where(income.c.id == current_income.id).values(**current_income.dict())
    await session.execute(new_version)
    await session.commit()

    return {"status": "success"}


@router.put("/expenses/")
async def edit_expense(current_expense: UpdateExpense, session: AsyncSession = Depends(get_async_session)):
    new_version = update(expense).where(expense.c.id == current_expense.id).values(**current_expense.dict())
    await session.execute(new_version)
    await session.commit()

    return {"status": "success"}


