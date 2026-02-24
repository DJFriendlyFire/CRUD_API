import uvicorn
from fastapi import FastAPI

from app.api.notes import r as router
from app.db import lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/index/")
async def get():
    return {"message": "index.html"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
