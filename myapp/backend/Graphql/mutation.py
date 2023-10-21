import strawberry
from Service.note import NoteService
from Service.daera_services import (
    PlayerService,
    TransactionService,
    GameInfoService,
    ResultService,
)

from schema import NoteType, NoteInput
from daera_schema import (
    PlayerType,
    PlayerInput,
    AllTransactionType,
    AllTransactionInput,
    GameInfoType,
    GameInfoInput,
    ResultOfPlayerType,
    ResultOfPlayerInput,
)
from uuid import UUID


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_note(self, note_data: NoteInput) -> NoteType:
        return await NoteService.add_note(note_data)

    @strawberry.mutation
    async def delete_note(self, note_id: int) -> str:
        return await NoteService.delete(note_id)

    @strawberry.mutation
    async def update_note(self, note_id: int, note_data: NoteInput) -> str:
        return await NoteService.update(note_id, note_data)

    # Player Mutations
    @strawberry.mutation
    async def create_player(self, player_data: PlayerInput) -> PlayerType:
        return await PlayerService.add_player(player_data)

    @strawberry.mutation
    async def delete_player(self, player_id: UUID) -> str:
        return await PlayerService.delete(player_id)

    @strawberry.mutation
    async def update_player(self, player_id: UUID, player_data: PlayerInput) -> str:
        return await PlayerService.update(player_id, player_data)

    # AllTransaction Mutations
    @strawberry.mutation
    async def create_transaction(
        self, transaction_data: AllTransactionInput
    ) -> AllTransactionType:
        return await TransactionService.add_transaction(transaction_data)

    @strawberry.mutation
    async def delete_transaction(self, transaction_id: UUID) -> str:
        return await TransactionService.delete(transaction_id)

    @strawberry.mutation
    async def update_transaction(
        self, transaction_id: UUID, transaction_data: AllTransactionInput
    ) -> str:
        return await TransactionService.update(transaction_id, transaction_data)

    # GameInfo Mutations
    @strawberry.mutation
    async def create_gameinfo(self, gameinfo_data: GameInfoInput) -> GameInfoType:
        return await GameInfoService.add_gameinfo(gameinfo_data)

    @strawberry.mutation
    async def delete_gameinfo(self, gameinfo_id: UUID) -> str:
        return await GameInfoService.delete(gameinfo_id)

    @strawberry.mutation
    async def update_gameinfo(
        self, gameinfo_id: UUID, gameinfo_data: GameInfoInput
    ) -> str:
        return await GameInfoService.update(gameinfo_id, gameinfo_data)

    # ResultOfPlayer Mutations
    @strawberry.mutation
    async def create_result(
        self, result_data: ResultOfPlayerInput
    ) -> ResultOfPlayerType:
        return await ResultService.add_result(result_data)

    @strawberry.mutation
    async def delete_result(self, result_id: UUID) -> str:
        return await ResultService.delete(result_id)

    @strawberry.mutation
    async def update_result(
        self, result_id: UUID, result_data: ResultOfPlayerInput
    ) -> str:
        return await ResultService.update(result_id, result_data)
