"""Added DateTime to incomes and expenses

Revision ID: 25695e88decc
Revises: 6f6abe4d574f
Create Date: 2023-12-09 11:30:19.871340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25695e88decc'
down_revision: Union[str, None] = '6f6abe4d574f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expense', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('income', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('income', 'date')
    op.drop_column('expense', 'date')
    # ### end Alembic commands ###