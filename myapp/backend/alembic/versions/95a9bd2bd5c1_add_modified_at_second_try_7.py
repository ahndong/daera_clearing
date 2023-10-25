"""add modified_at Second TRY - 7

Revision ID: 95a9bd2bd5c1
Revises: 48e16050739f
Create Date: 2023-10-25 10:29:11.230664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95a9bd2bd5c1'
down_revision: Union[str, None] = '48e16050739f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note', 'created_at')
    # ### end Alembic commands ###
