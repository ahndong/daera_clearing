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
    nickname: str
    totalbuyin: float
    totalout: float
    netscore: float
    noofgames: int
    getbbozziratio: float
    setbbozziratio: float


class AllTransaction(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    playerid: UUID = Field(foreign_key="player.id")
    transactiontype: TxType
    amount: float
    time: datetime = Field(default=datetime.now)


class GameInfo(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    netPlayer: int = Field()
    netBuyin: float = Field(default=0.0)
    netGamefee: float = Field(default=0.0)
    netBbozzi: float = Field(default=0.0)
    startAt: datetime = Field(default=datetime.now)
    finishAt: datetime = Field(None)
    playtimeMin: int = Field(None)


class ResultOfPlayer(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    gameinfoid: UUID = Field(foreign_key="gameinfo.id")
    playerid: UUID = Field(foreign_key="player.id")
    buyin: float
    chipout: float
    actualresult: float
    rankongame: int
