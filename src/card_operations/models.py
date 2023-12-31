from sqlalchemy import Column, Integer, String, Table, Float, ForeignKey

from src.auth.models import user
from src.database import metadata


type_card = Table(
    "type",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
)

card = Table(
    "card",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("type_id", Integer, ForeignKey(type_card.c.id)),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("balance", Float, nullable=False),
)
