"""Update models in card_operations

Revision ID: b9b22ffade2d
Revises: 0a985e99300e
Create Date: 2023-12-08 22:39:32.903075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision: str = 'b9b22ffade2d'
down_revision: Union[str, None] = '0a985e99300e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'incomes')
    op.drop_column('card', 'expenses')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('expenses', sqlite.JSON(), nullable=True))
    op.add_column('card', sa.Column('incomes', sqlite.JSON(), nullable=True))
    # ### end Alembic commands ###
