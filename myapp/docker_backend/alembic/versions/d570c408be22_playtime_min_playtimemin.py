"""playtime_min -> playtimeMin

Revision ID: d570c408be22
Revises: cad171cdb074
Create Date: 2023-10-23 16:23:46.379600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d570c408be22"
down_revision: Union[str, None] = "cad171cdb074"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "gameinfo",
        sa.Column("playtimeMin", sa.Integer(), server_default="0", nullable=True),
    )
    op.drop_column("gameinfo", "playtime_min")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "gameinfo",
        sa.Column("playtime_min", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.drop_column("gameinfo", "playtimeMin")
    # ### end Alembic commands ###
