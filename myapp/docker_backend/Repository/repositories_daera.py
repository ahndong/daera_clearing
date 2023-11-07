from Model.tables_daera import Player, TransactionLog, GameInfo, ResultOfPlayer
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete

from uuid import UUID
from typing import Optional


class PlayerRepository:
    @staticmethod
    async def create(player: Player):
        async with db as session:
            async with session.begin():
                session.add(player)
            await db.commit_rollback()

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(Player)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_id(player_id: UUID):
        async with db as session:
            stmt = select(Player).where(Player.id == player_id)
            result = await session.execute(stmt)
            player = result.scalars().first()
            return player

    @staticmethod
    async def get_by_nickname(nickname: str) -> Optional[Player]:
        async with db as session:
            stmt = select(Player).where(Player.nickname == nickname)
            result = await session.execute(stmt)
            player = result.scalars().first()
            return player

    @staticmethod
    async def update(player_id: UUID, player: Player) -> int:
        async with db as session:
            # ID가 수정되지 않는 방식
            values_to_update = {k: v for k, v in player.dict().items() if k != "id"}

            query = (
                sql_update(Player)
                .where(Player.id == player_id)
                .values(**values_to_update)
                .execution_options(synchronize_session="fetch")
            )

            result = await session.execute(query)
            await db.commit_rollback()
            return result.rowcount

    @staticmethod
    async def delete(player_id: UUID):
        async with db as session:
            query = sql_delete(Player).where(Player.id == player_id)
            await session.execute(query)
            await db.commit_rollback()


class TransactionLogRepository:
    @staticmethod
    async def create(transaction_data: TransactionLog):
        async with db as session:
            async with session.begin():
                session.add(transaction_data)
            await db.commit_rollback()

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(TransactionLog)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_id(transaction_id: UUID):
        async with db as session:
            stmt = select(TransactionLog).where(TransactionLog.id == transaction_id)
            result = await session.execute(stmt)
            transaction = result.scalars().first()
            return transaction

    @staticmethod
    async def update(transactionlog_id: UUID, transactionlog: TransactionLog) -> int:
        async with db as session:
            # ID가 수정되지 않는 방식
            value_to_update = {
                k: v for k, v in transactionlog.dict().items() if k != "id"
            }

            query = (
                sql_update(TransactionLog)
                .where(TransactionLog.id == transactionlog_id)
                .values(**value_to_update)
                .execution_options(synchronize_session="fetch")
            )
            result = await session.execute(query)
            await db.commit_rollback()
            return result.rowcount

    @staticmethod
    async def delete(transaction_id: UUID):
        async with db as session:
            query = sql_delete(TransactionLog).where(
                TransactionLog.id == transaction_id
            )
            await session.execute(query)
            await db.commit_rollback()


class GameInfoRepository:
    @staticmethod
    async def create(gameinfo: GameInfo):
        async with db as session:
            async with session.begin():
                session.add(gameinfo)
            await db.commit_rollback()

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(GameInfo)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_id(gameinfo_id: UUID):
        async with db as session:
            stmt = select(GameInfo).where(GameInfo.id == gameinfo_id)
            result = await session.execute(stmt)
            gameinfo = result.scalars().first()
            return gameinfo

    @staticmethod
    async def update(gameinfo_id: UUID, gameinfo: GameInfo) -> int:
        async with db as session:
            # # 수정할 때마다 ID가 수정되는 기존 방식
            # query = (
            #     sql_update(GameInfo)
            #     .where(GameInfo.id == gameinfo_id)
            #     .values(**gameinfo_data.dict())
            #     .execution_options(synchronize_session="fetch")
            # )

            # ID가 수정되지 않는 방식
            values_to_update = {k: v for k, v in gameinfo.dict().items() if k != "id"}

            query = (
                sql_update(GameInfo)
                .where(GameInfo.id == gameinfo_id)
                .values(**values_to_update)
                .execution_options(synchronize_session="fetch")
            )

            result = await session.execute(query)
            await db.commit_rollback()
            return result.rowcount

    @staticmethod
    async def delete(gameinfo_id: UUID):
        async with db as session:
            query = sql_delete(GameInfo).where(GameInfo.id == gameinfo_id)
            await session.execute(query)
            await db.commit_rollback()


class ResultRepository:
    @staticmethod
    async def create(result_data: ResultOfPlayer):
        async with db as session:
            async with session.begin():
                session.add(result_data)
            await db.commit_rollback()

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(ResultOfPlayer)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_id(result_id: UUID):
        async with db as session:
            stmt = select(ResultOfPlayer).where(ResultOfPlayer.id == result_id)
            result = await session.execute(stmt)
            result_data = result.scalars().first()
            return result_data

    @staticmethod
    async def update(result_id: UUID, result_data: ResultOfPlayer) -> int:
        async with db as session:
            value_to_update = {k: v for k, v in result_data.dict().items() if k != "id"}

            query = (
                sql_update(ResultOfPlayer)
                .where(ResultOfPlayer.id == result_id)
                .values(**value_to_update)
                .execution_options(synchronize_session="fetch")
            )

            result = await session.execute(query)
            await db.commit_rollback()
            return result.rowcount

    @staticmethod
    async def delete(result_id: UUID):
        async with db as session:
            query = sql_delete(ResultOfPlayer).where(ResultOfPlayer.id == result_id)
            await session.execute(query)
            await db
