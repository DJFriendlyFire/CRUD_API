from datetime import datetime

from pydantic import Field, BaseModel

from app.domain import Note


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    content: str = Field(min_length=1)


class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=50)
    content: str | None = Field(default=None, min_length=1)


class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_domain(n: Note) -> "NoteOut":
        return NoteOut(
            id=n.id,
            title=n.title,
            content=n.content,
            created_at=n.created_at,
            updated_at=n.updated_at,
        )
