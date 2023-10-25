from datetime import datetime
from sqlmodel import SQLModel, Field
from sqlalchemy.sql import text

from typing import Optional


class Note(SQLModel, table=True):
    __tablename__ = "note"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    name: str
    description: str
    # created_at: datetime = Field(default=datetime.now, nullable=False)
    created_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )
    modified_at: datetime = Field(
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")}
    )


# from sqlalchemy import Column, Integer, String, DateTime, Table, MetaData
# from sqlalchemy.sql import func
# from datetime import datetime

# import sqlalchemy as sa

# metadata = MetaData()

# Note = Table(
#     "note",
#     metadata,
#     Column("id", Integer, primary_key=True, nullable=False),
#     Column("name", String, nullable=False),
#     Column("description", String, nullable=False),
#     Column("created_at", DateTime, default=datetime.now, nullable=False),
#     Column("modified_at", DateTime, default=datetime.now, nullable=False),
#     Column(
#         "test_timestamp01_at",
#         DateTime,
#         server_default=sa.text("CURRENT_TIMESTAMP"),
#         nullable=False,
#     ),
# )
