import strawberry
from uuid import UUID
from datetime import datetime
from Model.daera_tables import TxType
from typing import Optional


@strawberry.type
class PlayerType:
    id: UUID
    nickname: str
    total_buyin: float = 0.0
    total_out: float = 0.0
    net_score: float = 0.0
    no_of_games: int = 0
    get_bbozzi_ratio: float = None
    set_bbozzi_ratio: float = None
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None


@strawberry.input
class PlayerInput:
    nickname: str
    total_buyin: float = 0.0
    total_out: float = 0.0
    net_score: float = 0.0
    no_of_games: int = 0
    get_bbozzi_ratio: float = None
    set_bbozzi_ratio: float = None


@strawberry.type
class TransactionLogType:
    id: UUID
    playerid: UUID
    transactiontype: TxType
    amount: float
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None


@strawberry.input
class TransactionLogInput:
    playerid: UUID
    transactiontype: TxType
    amount: float


# 아래에서 각 Optional이 있는 이유는 create 시에는 반환하는 GameInfoType에 각 해당 값이 있을 필요가 없기 때문
@strawberry.type
class GameInfoType:
    id: UUID
    net_player: int
    net_buyin: float
    net_gamefee: float
    net_bbozzi: float
    start_at: Optional[datetime] = None
    finish_at: Optional[datetime] = None
    playtime_min: int
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None


@strawberry.input
class GameInfoInput:
    net_player: int
    net_buyin: float
    net_gamefee: float
    net_bbozzi: float
    start_at: Optional[datetime] = None
    finish_at: Optional[datetime] = None
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
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None


@strawberry.input
class ResultOfPlayerInput:
    gameinfo_id: UUID
    player_id: UUID
    buyin: float
    chipout: float
    actual_result: float
    rank_on_game: int
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
