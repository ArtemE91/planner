from beanie import Document, Link

from pydantic import EmailStr
from models.events import Event

class User(Document):
    class Settings:
        name = "users"

    email: EmailStr
    username: str
    events: list[Link[Event]] | None = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "fastapi@packt.com",
                "username": "fastapi",
            }
        }
    }
