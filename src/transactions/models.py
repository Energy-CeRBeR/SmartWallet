from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey

from src.card_operations.models import card
from src.auth.models import user

metadata = MetaData()

in_category = Table(
    "income category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)

ex_category = Table(
    "expense category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("user_id", Integer, ForeignKey(user.c.id)),
)

income = Table(
    "income",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("category_id", Integer, ForeignKey(in_category.c.id)),
    Column("card_id", Integer, ForeignKey(card.c.id)),
    Column("amount", Integer),
)

expense = Table(
    "expense",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("category_id", Integer, ForeignKey(ex_category.c.id)),
    Column("card_id", Integer, ForeignKey(card.c.id)),
    Column("amount", Integer),
)