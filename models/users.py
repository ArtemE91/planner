from beanie import Document, Link

from pydantic import EmailStr, BaseModel
from models.events import Event


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class User(Document):
    class Settings:
        name = "users"

    email: EmailStr
    username: str
    password: str
    events: list[Link[Event]] | None = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "fastapi@packt.com",
                "username": "fastapi",
                "password": "my-password",
                "events": ["66ec10e01f81569c77be30a3"]
            }
        }
    }
