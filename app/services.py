from app.crud import Crud
from app.db import db
from app.schemas import NoteCreate, NoteUpdate


class NoteService:
    def __init__(self, crud: Crud):
        self._crud = crud

    async def create(self, note: NoteCreate):
        return await self._crud.create(title=note.title, content=note.content)

    async def get(self, note_id: int):
        return await self._crud.get(note_id=note_id)

    async def update(self, note_id: int, note: NoteUpdate):
        return await self._crud.update(
            note_id=note_id, title=note.title, content=note.content
        )

    async def delete(self, note_id: int):
        return await self._crud.delete(note_id=note_id)


crud = Crud(db=db)
note_services = NoteService(crud=crud)
