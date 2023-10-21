from Model.daera_tables import Player, AllTransaction, GameInfo, ResultOfPlayer
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete

from uuid import UUID


class PlayerRepository:
    @staticmethod
    async def create(player_data: Player):
        async with db as session:
            async with session.begin():
                session.add(player_data)
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
    async def update(player_id: UUID, player_data: Player):
        async with db as session:
            query = (
                sql_update(Player)
                .where(Player.id == player_id)
                .values(**player_data.dict())
                .execution_options(synchronize_session="fetch")
            )
            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(player_id: UUID):
        async with db as session:
            query = sql_delete(Player).where(Player.id == player_id)
            await session.execute(query)
            await db.commit_rollback()


class TransactionRepository:
    @staticmethod
    async def create(transaction_data: AllTransaction):
        async with db as session:
            async with session.begin():
                session.add(transaction_data)
            await db.commit_rollback()

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(AllTransaction)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_id(transaction_id: UUID):
        async with db as session:
            stmt = select(AllTransaction).where(AllTransaction.id == transaction_id)
            result = await session.execute(stmt)
            transaction = result.scalars().first()
            return transaction

    @staticmethod
    async def update(transaction_id: UUID, transaction_data: AllTransaction):
        async with db as session:
            query = (
                sql_update(AllTransaction)
                .where(AllTransaction.id == transaction_id)
                .values(**transaction_data.dict())
                .execution_options(synchronize_session="fetch")
            )
            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(transaction_id: UUID):
        async with db as session:
            query = sql_delete(AllTransaction).where(
                AllTransaction.id == transaction_id
            )
            await session.execute(query)
            await db.commit_rollback()


class GameInfoRepository:
    @staticmethod
    async def create(gameinfo_data: GameInfo):
        async with db as session:
            async with session.begin():
                session.add(gameinfo_data)
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
    async def update(gameinfo_id: UUID, gameinfo_data: GameInfo):
        async with db as session:
            query = (
                sql_update(GameInfo)
                .where(GameInfo.id == gameinfo_id)
                .values(**gameinfo_data.dict())
                .execution_options(synchronize_session="fetch")
            )
            await session.execute(query)
            await db.commit_rollback()

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
    async def update(result_id: UUID, result_data: ResultOfPlayer):
        async with db as session:
            query = (
                sql_update(ResultOfPlayer)
                .where(ResultOfPlayer.id == result_id)
                .values(**result_data.dict())
                .execution_options(synchronize_session="fetch")
            )
            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(result_id: UUID):
        async with db as session:
            query = sql_delete(ResultOfPlayer).where(ResultOfPlayer.id == result_id)
            await session.execute(query)
            await db
