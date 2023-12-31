from sqlalchemy import Column, Integer, String, Table, Date, Float, ForeignKey
from datetime import date

from src.card_operations.models import card
from src.auth.models import user
from src.database import metadata

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
    Column("amount", Float, nullable=False),
    Column("description", String),
    Column("date", Date, default=date.today()),
)

expense = Table(
    "expense",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("category_id", Integer, ForeignKey(ex_category.c.id)),
    Column("card_id", Integer, ForeignKey(card.c.id)),
    Column("amount", Float, nullable=False),
    Column("description", String),
    Column("date", Date, default=date.today()),
)
