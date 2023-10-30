import strawberry
from datetime import datetime


@strawberry.type
class NoteType:
    id: int
    name: str
    description: str
    created_at: datetime
    modified_at: datetime


@strawberry.input
class NoteInput:
    name: str
    description: str
