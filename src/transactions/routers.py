from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.card_operations.models import card, type_card
from src.transactions.schemas import CreateInCategory, CreateExCategory, CreateIncome, CreateExpense
from src.transactions.models import in_category, ex_category, income, expense

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)


@router.get("/in_categories/")
async def get_in_category(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(in_category).where(in_category.c.user_id == id)
    result = await session.execute(query)

    return result.mappings().all()


@router.get("/ex_categories/")
async def get_ex_category(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(ex_category).where(ex_category.c.user_id == id)
    result = await session.execute(query)

    return result.mappings().all()


@router.post("/in_categories/")
async def add_in_category(new_in_category: CreateInCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(in_category).values(**new_in_category.dict())
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.post("/ex_categories/")
async def add_ex_category(new_ex_category: CreateExCategory, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(ex_category).values(**new_ex_category.dict())
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.post("/in_categories/delete/")
async def del_in_category(category_id: int, session: AsyncSession = Depends(get_async_session)):
    to_delete = delete(in_category).where(in_category.c.id == category_id)
    await session.execute(to_delete)
    await session.commit()

    return {"status": "success"}


@router.post("/ex_categories/delete/")
async def del_ex_category(category_id: int, session: AsyncSession = Depends(get_async_session)):
    to_delete = delete(ex_category).where(ex_category.c.id == category_id)
    await session.execute(to_delete)
    await session.commit()

    return {"status": "success"}


@router.get("/incomes/")
async def get_income(card_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(income).where(income.c.card_id == card_id)
    result = await session.execute(query)

    return result.mappings().all()


@router.get("/expenses/")
async def get_expense(card_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(expense).where(expense.c.card_id == card_id)
    result = await session.execute(query)

    return result.mappings().all()


@router.post("/incomes/create/")
async def add_income(new_income: CreateIncome, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(income).values(**new_income.dict())
    card_update = update(card).where(card.c.id == new_income.card_id).values(
        balance=card.c.balance + new_income.amount)
    await session.execute(stmt)
    await session.execute(card_update)
    await session.commit()

    return {"status": "success"}


@router.post("/expenses/create/")
async def add_expense(new_expense: CreateExpense, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(expense).values(**new_expense.dict())
    card_update = update(card).where(card.c.id == new_expense.card_id).values(
        balance=card.c.balance - new_expense.amount)
    await session.execute(stmt)
    await session.execute(card_update)
    await session.commit()

    return {"status": "success"}


@router.post("/incomes/delete/")
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


@router.post("/expenses/delete/")
async def del_expense(expense_id: int, session: AsyncSession = Depends(get_async_session)):
    card_id = await session.execute(select(expense.c.card_id).where(expense.c.id == expense_id))
    amount = await session.execute(select(expense.c.amount).where(expense.c.id == expense_id))
    card_update = update(card).where(card.c.id == card_id.scalar()).values(
        balance=card.c.balance + amount.scalar())

    to_delete = delete(expense).where(expense.c.id == expense_id)
    await session.execute(to_delete)
    await session.execute(card_update)
    await session.commit()

    return {"status": "success"}


@router.post("/incomes/update/")
async def edit_income(current_income: CreateIncome, session: AsyncSession = Depends(get_async_session)):
    new_version = update(income).where(income.c.id == current_income.id).values(**current_income.dict())
    await session.execute(new_version)
    await session.commit()

    return {"status": "success"}


@router.post("/expenses/update/")
async def edit_expense(current_expense: CreateIncome, session: AsyncSession = Depends(get_async_session)):
    new_version = update(expense).where(expense.c.id == current_expense.id).values(**current_expense.dict())
    await session.execute(new_version)
    await session.commit()

    return {"status": "success"}


