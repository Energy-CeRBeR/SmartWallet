from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.card_operations.models import card, type_card
from src.transactions.schemas import CreateInCategory, CreateExCategory
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
