from typing import List

import strawberry

from Service.note import NoteService

from Service.daera_services import (
    PlayerService,
    TransactionLogService,
    GameInfoService,
    ResultOfPlayerService,
)

from schema import NoteType
from daera_schema import (
    PlayerType,
    TransactionLogType,
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

    # TransactionLog Queries
    @strawberry.field
    async def get_all_transactionlog(self) -> List[TransactionLogType]:
        return await TransactionLogService.get_all_transactionlog()

    @strawberry.field
    async def get_transactionlog_by_id(self, id: UUID) -> Optional[TransactionLogType]:
        return await TransactionLogService.get_transactionlog_by_id(id)

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
        return await ResultOfPlayerService.get_all_results()

    @strawberry.field
    async def get_result_by_id(self, id: UUID) -> Optional[ResultOfPlayerType]:
        return await ResultOfPlayerService.get_result_by_id(id)
