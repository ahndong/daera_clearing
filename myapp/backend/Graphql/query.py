from typing import List

import strawberry

from Service.note import NoteService

from Service.daera_services import (
    PlayerService,
    TransactionService,
    GameInfoService,
    ResultService,
)

from schema import NoteType
from daera_schema import (
    PlayerType,
    AllTransactionType,
    GameInfoType,
    ResultOfPlayerType,
)
from uuid import UUID
from typing import Optional


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World!"

    @strawberry.field
    async def get_all_noote(self) -> List[NoteType]:
        return await NoteService.get_all_note()

    @strawberry.field
    async def get_by_id(self, id: int) -> NoteType:
        return await NoteService.get_by_id(id)

    # Player Queries
    @strawberry.field
    async def get_all_players(self) -> List[PlayerType]:
        return await PlayerService.get_all_players()

    @strawberry.field
    async def get_player_by_id(self, id: UUID) -> Optional[PlayerType]:
        return await PlayerService.get_player_by_id(id)

    # AllTransaction Queries
    @strawberry.field
    async def get_all_transactions(self) -> List[AllTransactionType]:
        return await TransactionService.get_all_transactions()

    @strawberry.field
    async def get_transaction_by_id(self, id: UUID) -> Optional[AllTransactionType]:
        return await TransactionService.get_transaction_by_id(id)

    # GameInfo Queries
    @strawberry.field
    async def get_all_gameinfos(self) -> List[GameInfoType]:
        return await GameInfoService.get_all_gameinfos()

    @strawberry.field
    async def get_gameinfo_by_id(self, id: UUID) -> Optional[GameInfoType]:
        return await GameInfoService.get_gameinfo_by_id(id)

    # ResultOfPlayer Queries
    @strawberry.field
    async def get_all_results(self) -> List[ResultOfPlayerType]:
        return await ResultService.get_all_results()

    @strawberry.field
    async def get_result_by_id(self, id: UUID) -> Optional[ResultOfPlayerType]:
        return await ResultService.get_result_by_id(id)
