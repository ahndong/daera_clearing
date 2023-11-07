from Model.tables_daera import Player, TransactionLog, GameInfo, ResultOfPlayer
from Repository.repositories_daera import (
    PlayerRepository,
    TransactionLogRepository,
    GameInfoRepository,
    ResultRepository,
)
from schema_daera import (
    PlayerInput,
    PlayerType,
    TransactionLogInput,
    TransactionLogType,
    GameInfoInput,
    GameInfoType,
    ResultOfPlayerInput,
    ResultOfPlayerType,
)
from uuid import UUID
from datetime import datetime


class PlayerService:
    @staticmethod
    async def add_player(player_input_data: PlayerInput):
        # 중복 검사
        existing_player = await PlayerRepository.get_by_nickname(
            player_input_data.nickname
        )
        if existing_player:
            raise ValueError(
                f"Nickname '{player_input_data.nickname}' is already in use."
            )

        player_input_dict = player_input_data.__dict__
        player = Player(
            **player_input_dict,
        )
        await PlayerRepository.create(player)

        player_input_data = {
            key: value
            for key, value in player.__dict__.items()
            if not key.startswith("_sa_")
        }

        return PlayerType(**player_input_data)

    @staticmethod
    async def get_all_players():
        return await PlayerRepository.get_all()

    @staticmethod
    async def get_player_by_id(player_id: UUID):
        return await PlayerRepository.get_by_id(player_id)

    @staticmethod
    async def update(player_id: UUID, player_input_data: PlayerInput):
        player = Player(**player_input_data.__dict__)

        updated_rows = await PlayerRepository.update(player_id, player)

        if updated_rows == 0:
            return f"No player found with id {player_id}. Update failed."
        return f"Successfully updated player with id {player_id}!"

    @staticmethod
    async def delete(player_id: UUID):
        await PlayerRepository.delete(player_id)
        return f"Successfully deleted player with id {player_id}"


class TransactionLogService:
    @staticmethod
    async def add_transactionlog(transactionlog_input_data: TransactionLogInput):
        transactionlog_input_dict = transactionlog_input_data.__dict__
        transactionlog = TransactionLog(
            **transactionlog_input_dict,
        )
        await TransactionLogRepository.create(transactionlog)

        transactionlog_input_data = {
            key: value
            for key, value in transactionlog.__dict__.items()
            if not key.startswith("_sa_")
        }

        return TransactionLogType(**transactionlog_input_data)

    @staticmethod
    async def get_all_transactionlog():
        return await TransactionLogRepository.get_all()

    @staticmethod
    async def get_transactionlog_by_id(transaction_id: UUID):
        return await TransactionLogRepository.get_by_id(transaction_id)

    @staticmethod
    async def update(
        transactionlog_id: UUID, transactionlog_input_data: TransactionLogInput
    ):
        transactionlog = TransactionLog(**transactionlog_input_data.__dict__)

        updated_rows = await TransactionLogRepository.update(
            transactionlog_id, transactionlog
        )

        if updated_rows == 0:
            return (
                f"No TransactionLog found with id {transactionlog_id}. Update failed."
            )
        return f"Successfully updated TransactionLog with id {transactionlog_id}"

    @staticmethod
    async def delete(transaction_id: UUID):
        await TransactionLogRepository.delete(transaction_id)
        return f"Successfully deleted TransactionLog with id {transaction_id}"


class GameInfoService:
    @staticmethod
    async def add_gameinfo(gameinfo_input_data: GameInfoInput):
        gameinfo_input_dict = gameinfo_input_data.__dict__
        gameinfo = GameInfo(
            **gameinfo_input_dict,
        )
        await GameInfoRepository.create(gameinfo)

        gameinfo_input_data = {
            key: value
            for key, value in gameinfo.__dict__.items()
            if not key.startswith("_sa_")
        }

        # 'start_at'과 'finish_at' 속성에 명시적으로 값을 설정하는 방법
        # gameinfo_input_data["start_at"] = datetime.now()
        # gameinfo_input_data["finish_at"] = datetime.now()

        return GameInfoType(**gameinfo_input_data)

    @staticmethod
    async def get_all_gameinfos():
        return await GameInfoRepository.get_all()

    @staticmethod
    async def get_gameinfo_by_id(gameinfo_id: UUID):
        return await GameInfoRepository.get_by_id(gameinfo_id)

    @staticmethod
    async def update(gameinfo_id: UUID, gameinfo_input_data: GameInfoInput):
        gameinfo = GameInfo(**gameinfo_input_data.__dict__)

        updated_rows = await GameInfoRepository.update(gameinfo_id, gameinfo)

        if updated_rows == 0:
            return f"No gameinfo found with id {gameinfo_id}. Update failed."
        return f"Successfully updated gameinfo with id {gameinfo_id}"

        # await GameInfoRepository.update(gameinfo_id, gameinfo)
        # return f"Successfully updated gameinfo with id {gameinfo_id}"

    @staticmethod
    async def delete(gameinfo_id: UUID):
        await GameInfoRepository.delete(gameinfo_id)
        return f"Successfully deleted gameinfo with id {gameinfo_id}"


class ResultOfPlayerService:
    @staticmethod
    async def add_result(result_input_data: ResultOfPlayerInput):
        result_input_dict = result_input_data.__dict__
        result = ResultOfPlayer(
            **result_input_dict,
        )
        await ResultRepository.create(result)

        result_input_data = {
            key: value
            for key, value in result.__dict__.items()
            if not key.startswith("_sa_")
        }

        return ResultOfPlayerType(**result_input_data)

    @staticmethod
    async def get_all_results():
        return await ResultRepository.get_all()

    @staticmethod
    async def get_result_by_id(result_id: UUID):
        return await ResultRepository.get_by_id(result_id)

    @staticmethod
    async def update(result_id: UUID, result_input_data: ResultOfPlayerInput):
        result = ResultOfPlayer(**result_input_data.__dict__)

        updated_rows = await ResultRepository.update(result_id, result)

        if updated_rows == 0:
            return f"No result found with id {result_id}. Update failed."
        return f"Successfully updated result with id {result_id}"

    @staticmethod
    async def delete(result_id: UUID):
        await ResultRepository.delete(result_id)
        return f"Successfully deleted result with id {result_id}"
