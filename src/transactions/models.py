from sqlalchemy import Column, Integer, String, Table, DateTime, MetaData, ForeignKey
from datetime import datetime

from src.card_operations.models import card
from src.auth.models import user

metadata = MetaData()

in_category = Table(
    "income category",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)

ex_category = Table(
    "expense category",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)

income = Table(
    "income",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("category_id", Integer, ForeignKey(in_category.c.id)),
    Column("card_id", Integer, ForeignKey(card.c.id)),
    Column("amount", Integer, nullable=False),
    Column("description", String),
    Column("date", DateTime, default=datetime.now()),
)

expense = Table(
    "expense",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("category_id", Integer, ForeignKey(ex_category.c.id)),
    Column("card_id", Integer, ForeignKey(card.c.id)),
    Column("amount", Integer, nullable=False),
    Column("description", String),
    Column("date", DateTime, default=datetime.now()),
)
