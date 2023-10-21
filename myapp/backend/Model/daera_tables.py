from datetime import datetime
from enum import Enum
from sqlmodel import Field, SQLModel, create_engine
from uuid import UUID, uuid4
import strawberry


@strawberry.enum
class TxType(str, Enum):
    buyin = "buyin"
    endchip = "endchip"
    setbbozzi = "setbbozzi"
    getbbozzi = "getbbozzi"
    gamefee = "gamefee"


class Player(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nickName: str
    totalBuyin: float
    totalOut: float
    netScore: float
    noOfGames: int
    getBbozziRatio: float
    setBbozziRatio: float


class AllTransaction(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    playerId: UUID = Field(foreign_key="player.id")
    transactionType: TxType
    amount: float
    time: datetime = Field(default=datetime.now)


class GameInfo(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    netPlayer: int
    netBuyin: float
    netGameFee: float
    netBbozzi: float
    start: datetime = Field(default=datetime.now)
    finish: datetime
    playTimeMin: int


class ResultOfPlayer(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    gameInfoId: UUID = Field(foreign_key="gameinfo.id")
    playerId: UUID = Field(foreign_key="player.id")
    buyIn: float
    chipOut: float
    actualResult: float
    rankOnGame: int
