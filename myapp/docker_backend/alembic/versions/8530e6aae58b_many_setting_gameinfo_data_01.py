"""many setting gameinfo data_01

Revision ID: 8530e6aae58b
Revises: 91678e531059
Create Date: 2023-10-25 12:15:30.549940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8530e6aae58b'
down_revision: Union[str, None] = '91678e531059'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alltransaction', sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.add_column('alltransaction', sa.Column('modified_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.drop_column('alltransaction', 'time')
    op.add_column('gameinfo', sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.add_column('gameinfo', sa.Column('modified_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.add_column('resultofplayer', sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    op.add_column('resultofplayer', sa.Column('modified_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resultofplayer', 'modified_at')
    op.drop_column('resultofplayer', 'created_at')
    op.drop_column('gameinfo', 'modified_at')
    op.drop_column('gameinfo', 'created_at')
    op.add_column('alltransaction', sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('alltransaction', 'modified_at')
    op.drop_column('alltransaction', 'created_at')
    # ### end Alembic commands ###
