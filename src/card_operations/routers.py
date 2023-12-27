from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.card_operations.models import card, type_card
from src.card_operations.schemas import TypeCreate, CardCreate, CardUpdate
from src.auth.base_config import current_user

router = APIRouter(
    prefix="/cards",
    tags=["cards"],
    dependencies=[Depends(current_user)]
)


@router.get("/")
async def get_card(user=Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(card).where(card.c.user_id == user.id)
    result = await session.execute(query)

    return result.mappings().all()


@router.post("/type/")
async def add_type(new_type: TypeCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(type_card).values(**new_type.dict())

    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.post("/")
async def add_card(new_card: CardCreate, user=Depends(current_user),
                   session: AsyncSession = Depends(get_async_session)):
    new_card = new_card.dict()
    new_card["user_id"] = user.id
    stmt = insert(card).values(**new_card)
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.delete("/")
async def del_card(card_id: int, user=Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    to_delete = delete(card).where(card.c.id == card_id and card.c.user_id == user.id)
    await session.execute(to_delete)
    await session.commit()

    return {"status": "success"}


@router.put("/")
async def update_card(current_card: CardUpdate, user=Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    new_version = update(card).where(card.c.id == current_card.id
                                     and card.c.user_id == user.id).values(**current_card.dict())
    await session.execute(new_version)
    await session.commit()

    return {"status": "success"}
