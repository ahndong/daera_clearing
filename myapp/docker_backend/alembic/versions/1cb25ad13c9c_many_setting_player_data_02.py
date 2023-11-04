"""many setting player data_02

Revision ID: 1cb25ad13c9c
Revises: 3135bdf5e17c
Create Date: 2023-10-25 19:41:54.041489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cb25ad13c9c'
down_revision: Union[str, None] = '3135bdf5e17c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'player', ['nickname'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'player', type_='unique')
    # ### end Alembic commands ###