from Model.daera_tables import Player, AllTransaction, GameInfo, ResultOfPlayer
from Repository.daera_repositories import (
    PlayerRepository,
    TransactionRepository,
    GameInfoRepository,
    ResultRepository,
)
from daera_schema import (
    PlayerInput,
    AllTransactionInput,
    GameInfoInput,
    ResultOfPlayerInput,
)
from uuid import UUID


class PlayerService:
    @staticmethod
    async def add_player(player_data: PlayerInput):
        player = Player(**player_data.dict())
        await PlayerRepository.create(player)
        return player

    @staticmethod
    async def get_all_players():
        return await PlayerRepository.get_all()

    @staticmethod
    async def get_player_by_id(player_id: UUID):
        return await PlayerRepository.get_by_id(player_id)

    @staticmethod
    async def update(player_id: UUID, player_data: PlayerInput):
        player = Player(**player_data.dict())
        await PlayerRepository.update(player_id, player)
        return f"Successfully updated player with id {player_id}"

    @staticmethod
    async def delete(player_id: UUID):
        await PlayerRepository.delete(player_id)
        return f"Successfully deleted player with id {player_id}"


class TransactionService:
    @staticmethod
    async def add_transaction(transaction_data: AllTransactionInput):
        transaction = AllTransaction(**transaction_data.dict())
        await TransactionRepository.create(transaction)
        return transaction

    @staticmethod
    async def get_all_transactions():
        return await TransactionRepository.get_all()

    @staticmethod
    async def get_transaction_by_id(transaction_id: UUID):
        return await TransactionRepository.get_by_id(transaction_id)

    @staticmethod
    async def update(transaction_id: UUID, transaction_data: AllTransactionInput):
        transaction = AllTransaction(**transaction_data.dict())
        await TransactionRepository.update(transaction_id, transaction)
        return f"Successfully updated transaction with id {transaction_id}"

    @staticmethod
    async def delete(transaction_id: UUID):
        await TransactionRepository.delete(transaction_id)
        return f"Successfully deleted transaction with id {transaction_id}"


class GameInfoService:
    @staticmethod
    async def add_gameinfo(gameinfo_data: GameInfoInput):
        gameinfo = GameInfo(**gameinfo_data.dict())
        await GameInfoRepository.create(gameinfo)
        return gameinfo

    @staticmethod
    async def get_all_gameinfos():
        return await GameInfoRepository.get_all()

    @staticmethod
    async def get_gameinfo_by_id(gameinfo_id: UUID):
        return await GameInfoRepository.get_by_id(gameinfo_id)

    @staticmethod
    async def update(gameinfo_id: UUID, gameinfo_data: GameInfoInput):
        gameinfo = GameInfo(**gameinfo_data.dict())
        await GameInfoRepository.update(gameinfo_id, gameinfo)
        return f"Successfully updated gameinfo with id {gameinfo_id}"

    @staticmethod
    async def delete(gameinfo_id: UUID):
        await GameInfoRepository.delete(gameinfo_id)
        return f"Successfully deleted gameinfo with id {gameinfo_id}"


class ResultService:
    @staticmethod
    async def add_result(result_data: ResultOfPlayerInput):
        result = ResultOfPlayer(**result_data.dict())
        await ResultRepository.create(result)
        return result

    @staticmethod
    async def get_all_results():
        return await ResultRepository.get_all()

    @staticmethod
    async def get_result_by_id(result_id: UUID):
        return await ResultRepository.get_by_id(result_id)

    @staticmethod
    async def update(result_id: UUID, result_data: ResultOfPlayerInput):
        result = ResultOfPlayer(**result_data.dict())
        await ResultRepository.update(result_id, result)
        return f"Successfully updated result with id {result_id}"

    @staticmethod
    async def delete(result_id: UUID):
        await ResultRepository.delete(result_id)
        return f"Successfully deleted result with id {result_id}"
