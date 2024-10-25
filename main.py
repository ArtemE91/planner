import uvicorn
from fastapi import FastAPI

from database.connection import lifespan
from routes.users import user_router
from routes.events import event_router


app = FastAPI(lifespan=lifespan)


app.include_router(user_router, prefix="/users")
app.include_router(event_router, prefix="/events")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)