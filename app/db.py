from contextlib import asynccontextmanager

from fastapi import FastAPI
from psycopg_pool import AsyncConnectionPool

from app.settings import DATABASE_URL


class Db:
    def __init__(self, db_url: str):
        self._pool = AsyncConnectionPool(
            conninfo=db_url, min_size=1, max_size=10, open=False
        )

    async def open(self):
        await self._pool.open()

    async def close(self):
        await self._pool.close()

    def conn(self):
        return self._pool.connection()


db = Db(DATABASE_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.open()
    try:
        yield
    finally:
        await db.close()
