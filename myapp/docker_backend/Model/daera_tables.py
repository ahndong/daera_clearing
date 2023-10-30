from datetime import datetime
from enum import Enum
from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy.sql import text
from uuid import UUID, uuid4
import strawberry

from pydantic import validator


@strawberry.enum
class TxType(str, Enum):
    buyin = "buyin"
    endchip = "endchip"
    setbbozzi = "setbbozzi"
    getbbozzi = "getbbozzi"
    gamefee = "gamefee"


class Player(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nickname: str = Field(nullable=False, unique=True)
    total_buyin: float = Field(default=0.0)
    total_out: float = Field(default=0.0)
    net_score: float = Field(nullable=True)
    no_of_games: int = Field(default=0)
    get_bbozzi_ratio: float = Field(nullable=True)
    set_bbozzi_ratio: float = Field(nullable=True)
    created_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )
    modified_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )

    @validator("nickname", pre=True, always=True)
    def validate_nickname_length(cls, nickname):
        if len(nickname) < 2:
            raise ValueError("Nickname should be at least 2 characters longg")
        return nickname


class TransactionLog(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    playerid: UUID = Field(nullable=False, foreign_key="player.id")
    transactiontype: TxType = Field(nullable=False)
    amount: float = Field(nullable=False)
    created_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )
    modified_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )


class GameInfo(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    net_player: int = Field(default=2.0)
    net_buyin: float = Field(default=0.0)
    net_gamefee: float = Field(default=0.0)
    net_bbozzi: float = Field(default=0.0)
    start_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}, nullable=True
    )
    finish_at: datetime = Field(nullable=True)
    playtime_min: int = Field(None)
    created_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )
    modified_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )


# 각 개별 게임에서의 개별 선수의 성적에 대한 것
# 평균 게임별 참가자의 수 X 전체 게임 수 만큼의 row가 생길 것
class ResultOfPlayer(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    gameinfo_id: UUID = Field(nullable=False, foreign_key="gameinfo.id")
    player_id: UUID = Field(nullable=False, foreign_key="player.id")
    buyin: float
    chipout: float
    actual_result: float
    rank_on_game: int
    created_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )
    modified_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )
