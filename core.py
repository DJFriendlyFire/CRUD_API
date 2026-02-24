import uvicorn

from app import main

app = main.app

if __name__ == "__main__":
    uvicorn.run("core:app", reload=True)
