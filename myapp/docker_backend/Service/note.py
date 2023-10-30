from Model.note import Note
from Repository.note import NoteRepository
from schema import NoteInput, NoteType
from datetime import datetime


class NoteService:
    @staticmethod
    async def add_note(note_input_data: NoteInput):
        # # 결국 이거는 못쓰는게 맞는거 같다.
        # # SQLModel도 SQLAlchemy도 dict()를 지원하지 않는다.
        # note = Note(**note_data.dict())
        # await NoteRepository.create(note)

        # # 이것은 기본형 코드
        # note = Note()
        # note.name = note_data.name
        # note.description = note_data.description
        # note.created_at = datetime.now()
        # note.modified_at = datetime.now()
        # await NoteRepository.create(note)

        # NoteInput을 Note로 변환
        # 와우! 이것을 드디어 찾!았!다!
        note_dict = note_input_data.__dict__
        note = Note(**note_dict, created_at=datetime.now(), modified_at=datetime.now())
        await NoteRepository.create(note)

        # return NoteType(
        #     id=note.id,
        #     name=note.name,
        #     description=note.description,
        #     created_at=note.created_at,
        #     modified_at=note.modified_at,
        # )

        # note.__dict__는 SQLAlchemy 모델 객체의 모든 속성을 포함하며, 이 중 _sa_instance_state는 SQLAlchemy의 내부 상태를 나타내는 특별한 속성입니다. 이 속성은 NoteType에는 없기 때문에 위와 같은 오류가 발생합니다.
        # 이 문제를 해결하기 위해 _sa_instance_state와 같은 SQLAlchemy의 내부 속성을 제외하고 NoteType을 초기화해야 합니다.
        #  note.__dict__에서 _sa_로 시작하는 키를 제외하고 NoteType을 초기화하는 방법을 보여줍니다.
        note_input_data = {
            key: value
            for key, value in note.__dict__.items()
            if not key.startswith("_sa_")
        }

        # gameinfo_data 로그 확인
        print(
            "----------------------------------note, note_data----------------------------------"
        )
        print(note)
        print(note_input_data)
        print(
            "----------------------------------note, note_data----------------------------------"
        )

        return NoteType(**note_input_data)

    @staticmethod
    async def get_all_note():
        list_note = await NoteRepository.get_all()
        return [
            NoteType(
                id=note.id,
                name=note.name,
                description=note.description,
                created_at=note.created_at,
                modified_at=note.modified_at,
            )
            for note in list_note
        ]

    @staticmethod
    async def get_by_id(note_id: int):
        note = await NoteRepository.get_by_id(note_id)
        return NoteType(
            id=note.id,
            name=note.name,
            description=note.description,
            created_at=note.created_at,
            modified_at=note.modified_at,
        )

    @staticmethod
    async def update(note_id: int, note_data: NoteInput):
        note = Note()
        note.name = note_data.name
        note.description = note_data.description
        note.modified_at = datetime.now()
        await NoteRepository.update(note_id, note)

        return f"Successfully updated data by id {note_id}"

    @staticmethod
    async def delete(note_id: int):
        await NoteRepository.delete(note_id)
        return f"Successfully deleted data by id {note_id}"
