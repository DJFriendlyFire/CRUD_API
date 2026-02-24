from fastapi import APIRouter

from app.schemas import NoteUpdate, NoteCreate
from app.services import note_services

r = APIRouter(prefix="/notes")


@r.post("/create/")
async def create(note: NoteCreate):
    result = await note_services.create(note=note)
    return {"message": "access", "result": result}


@r.get("/{note_id}/")
async def get(note_id: int):
    result = await note_services.get(note_id=note_id)
    return {"message": "access", "result": result}


@r.put("/{note_id}/")
async def update(note_id: int, note: NoteUpdate):
    result = await note_services.update(note_id=note_id, note=note)
    return {"message": "access", "result": result}


@r.delete("/{note_id}/")
async def delete(note_id: int):
    result = await note_services.delete(note_id=note_id)
    return {"message": "access", "result": result}
