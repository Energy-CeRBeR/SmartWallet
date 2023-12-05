from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey, JSON

from src.auth.models import user

metadata = MetaData()

type_card = Table(
    "type",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

card = Table(
    "card",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("type_id", Integer, ForeignKey(type_card.c.id)),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("balance", Integer, nullable=False),
    Column("incomes", JSON, default=[]),
    Column("expenses", JSON, default=[]),
)