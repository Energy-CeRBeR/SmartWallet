"""Some updates in models

Revision ID: c012e63a0ec2
Revises: 3e960932a0cc
Create Date: 2023-12-31 21:53:48.980432

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c012e63a0ec2'
down_revision: Union[str, None] = '3e960932a0cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('card', 'balance',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('expense', 'amount',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('expense', 'date',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
    op.alter_column('income', 'amount',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('income', 'date',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('income', 'date',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)
    op.alter_column('income', 'amount',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('expense', 'date',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)
    op.alter_column('expense', 'amount',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('card', 'balance',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###