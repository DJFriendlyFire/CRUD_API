from app.db import Db


class Crud:
    def __init__(self, db: Db):
        self._db = db

    async def create(self, title: str, content: str):
        async with self._db.conn() as con:
            async with con.transaction():
                async with con.cursor() as cur:
                    await cur.execute(
                        """
                        INSERT INTO notes (title, content)
                        VALUES (%s, %s)
                        RETURNING id, title, content, created_at, updated_at;
                        """,
                        (title, content),
                    )
                    result = await cur.fetchone()
                    return result

    async def get(self, note_id: int):
        async with self._db.conn() as con:
            async with con.cursor() as cur:
                await cur.execute(
                    """
                    SELECT id, title, content, created_at, updated_at
                    FROM notes
                    WHERE id = %s;
                    """,
                    (note_id,),
                )
                result = await cur.fetchone()
                return result

    async def update(self, note_id: int, title: str | None, content: str | None):
        async with self._db.conn() as con:
            async with con.transaction():
                async with con.cursor() as cur:
                    await cur.execute(
                        """
                        UPDATE notes
                        SET title = COALESCE(%s, title),
                            content = COALESCE(%s, content),
                            updated_at = now()
                        WHERE id = %s
                        RETURNING id, title, content, created_at, updated_at; 
                        """,
                        (title, content, note_id),
                    )
                    result = await cur.fetchone()
                    return result

    async def delete(self, note_id: int):
        async with self._db.conn() as con:
            async with con.transaction():
                async with con.cursor() as cur:
                    await cur.execute(
                        """
                        DELETE FROM notes WHERE id = %s RETURNING id;
                        """,
                        (note_id,),
                    )
                    result = await cur.fetchone()
                    return result
