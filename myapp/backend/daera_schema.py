import strawberry
from uuid import UUID
from datetime import datetime
from Model.daera_tables import TxType


@strawberry.type
class PlayerType:
    id: UUID
    nickName: str
    totalBuyin: float
    totalOut: float
    netScore: float
    noOfGames: int
    getBbozziRatio: float
    setBbozziRatio: float


@strawberry.input
class PlayerInput:
    nickName: str
    totalBuyin: float
    totalOut: float
    netScore: float
    noOfGames: int
    getBbozziRatio: float
    setBbozziRatio: float


@strawberry.type
class AllTransactionType:
    id: UUID
    playerId: UUID
    transactionType: TxType
    amount: float
    time: datetime


@strawberry.input
class AllTransactionInput:
    playerId: UUID
    transactionType: TxType
    amount: float


@strawberry.type
class GameInfoType:
    id: UUID
    netPlayer: int
    netBuyin: float
    netGameFee: float
    netBbozzi: float
    start: datetime
    finish: datetime
    playTimeMin: int


@strawberry.input
class GameInfoInput:
    netPlayer: int
    netBuyin: float
    netGameFee: float
    netBbozzi: float
    finish: datetime
    playTimeMin: int


@strawberry.type
class ResultOfPlayerType:
    id: UUID
    gameInfoId: UUID
    playerId: UUID
    buyIn: float
    chipOut: float
    actualResult: float
    rankOnGame: int


@strawberry.input
class ResultOfPlayerInput:
    gameInfoId: UUID
    playerId: UUID
    buyIn: float
    chipOut: float
    actualResult: float
    rankOnGame: int
