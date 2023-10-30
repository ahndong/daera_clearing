"""many setting transactionlog data_01

Revision ID: a625a4fd95aa
Revises: 1cb25ad13c9c
Create Date: 2023-10-25 20:23:00.776585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a625a4fd95aa'
down_revision: Union[str, None] = '1cb25ad13c9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alltransaction')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alltransaction',
    sa.Column('id', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('playerid', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('transactiontype', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('amount', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('modified_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['playerid'], ['player.id'], name='alltransaction_playerid_fkey'),
    sa.PrimaryKeyConstraint('id', name='alltransaction_pkey')
    )
    # ### end Alembic commands ###
