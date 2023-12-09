from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.card_operations.models import card, type_card
from src.card_operations.schemas import TypeCreate, CardCreate

router = APIRouter(
    prefix="/cards",
    tags=["cards"]
)


@router.get("/")
async def get_card(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(card).where(card.c.user_id == id)
    result = await session.execute(query)

    return result.mappings().all()


@router.post("/type/")
async def add_type(new_type: TypeCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(type_card).values(**new_type.dict())
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.post("/")
async def add_card(new_card: CardCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(card).values(**new_card.dict())
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.post("/delete/")
async def del_card(card_id: int, session: AsyncSession = Depends(get_async_session)):
    to_delete = delete(card).where(card.c.id == card_id)
    await session.execute(to_delete)
    await session.commit()

    return {"status": "success"}


@router.post("/update/")
async def update_card(current_card: CardCreate, session: AsyncSession = Depends(get_async_session)):
    new_version = update(card).where(card.c.id == current_card.id).values(**current_card.dict())
    await session.execute(new_version)
    await session.commit()

    return {"status": "success"}
