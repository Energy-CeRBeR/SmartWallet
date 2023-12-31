"""added 'description' to transactions models

Revision ID: 6f6abe4d574f
Revises: b9b22ffade2d
Create Date: 2023-12-08 22:57:57.527870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f6abe4d574f'
down_revision: Union[str, None] = 'b9b22ffade2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('expense', sa.Column('description', sa.String(), nullable=True))
    op.add_column('income', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('income', 'description')
    op.drop_column('expense', 'description')
    # ### end Alembic commands ###