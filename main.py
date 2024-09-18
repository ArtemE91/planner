import uvicorn
from fastapi import FastAPI

from routers.users import user_router
from routers.events import event_router


app = FastAPI()
app.include_router(user_router, prefix="/users")
app.include_router(event_router, prefix="/events")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
