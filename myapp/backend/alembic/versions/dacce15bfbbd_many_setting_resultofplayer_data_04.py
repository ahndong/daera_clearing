"""many setting resultofplayer data_04

Revision ID: dacce15bfbbd
Revises: fca1743279e7
Create Date: 2023-10-25 20:51:23.843328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = "dacce15bfbbd"
down_revision: Union[str, None] = "fca1743279e7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "player",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
    )
    op.add_column(
        "player",
        sa.Column(
            "modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
    )
    op.add_column(
        "resultofplayer",
        sa.Column("gameinfo_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
    )
    op.add_column(
        "resultofplayer",
        sa.Column("player_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
    )
    op.add_column(
        "resultofplayer", sa.Column("actual_result", sa.Float(), nullable=False)
    )
    op.add_column(
        "resultofplayer", sa.Column("rank_on_game", sa.Integer(), nullable=False)
    )
    op.drop_constraint(
        "resultofplayer_playerid_fkey", "resultofplayer", type_="foreignkey"
    )
    op.drop_constraint(
        "resultofplayer_gameinfoid_fkey", "resultofplayer", type_="foreignkey"
    )
    op.create_foreign_key(None, "resultofplayer", "player", ["player_id"], ["id"])
    op.create_foreign_key(None, "resultofplayer", "gameinfo", ["gameinfo_id"], ["id"])
    op.drop_column("resultofplayer", "playerid")
    op.drop_column("resultofplayer", "rankongame")
    op.drop_column("resultofplayer", "actualresult")
    op.drop_column("resultofplayer", "gameinfoid")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "resultofplayer",
        sa.Column("gameinfoid", postgresql.UUID(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "resultofplayer",
        sa.Column(
            "actualresult",
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "resultofplayer",
        sa.Column("rankongame", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "resultofplayer",
        sa.Column("playerid", postgresql.UUID(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "resultofplayer", type_="foreignkey")
    op.drop_constraint(None, "resultofplayer", type_="foreignkey")
    op.create_foreign_key(
        "resultofplayer_gameinfoid_fkey",
        "resultofplayer",
        "gameinfo",
        ["gameinfoid"],
        ["id"],
    )
    op.create_foreign_key(
        "resultofplayer_playerid_fkey", "resultofplayer", "player", ["playerid"], ["id"]
    )
    op.drop_column("resultofplayer", "rank_on_game")
    op.drop_column("resultofplayer", "actual_result")
    op.drop_column("resultofplayer", "player_id")
    op.drop_column("resultofplayer", "gameinfo_id")
    op.drop_column("player", "modified_at")
    op.drop_column("player", "created_at")
    # ### end Alembic commands ###