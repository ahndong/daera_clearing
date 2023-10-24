import strawberry
from uuid import UUID
from datetime import datetime
from Model.daera_tables import TxType


@strawberry.type
class PlayerType:
    id: UUID
    nickname: str
    totalbuyin: float
    totalout: float
    netscore: float
    noofgames: int
    getbbozziratio: float
    setbbozziratio: float


@strawberry.input
class PlayerInput:
    nickname: str
    totalbuyin: float
    totalout: float
    netscore: float
    noofgames: int
    getbbozziratio: float
    setbbozziratio: float


@strawberry.type
class AllTransactionType:
    id: UUID
    playerid: UUID
    transactiontype: TxType
    amount: float
    time: datetime


@strawberry.input
class AllTransactionInput:
    playerid: UUID
    transactiontype: TxType
    amount: float


@strawberry.type
class GameInfoType:
    id: UUID
    net_player: int
    net_buyin: float
    net_gamefee: float
    net_bbozzi: float
    start_at: datetime
    finish_at: datetime
    playtime_min: int


@strawberry.input
class GameInfoInput:
    net_player: int
    net_buyin: float
    net_gamefee: float
    net_bbozzi: float
    finish_at: datetime
    playtime_min: int


@strawberry.type
class ResultOfPlayerType:
    id: UUID
    gameinfoid: UUID
    playerid: UUID
    buyin: float
    chipout: float
    actualresult: float
    rankongame: int


@strawberry.input
class ResultOfPlayerInput:
    gameinfoid: UUID
    playerid: UUID
    buyin: float
    chipout: float
    actualresult: float
    rankongame: int
