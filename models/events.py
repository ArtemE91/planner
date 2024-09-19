from beanie import Document
from pydantic import BaseModel


class Event(Document):

    class Settings:
        name = "events"

    title: str | None = None
    description: str | None = None
    tags: list[str] | None = None
    location: str | None = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "FastAPI Book Launch",
                "description": "We will be discussing the contents of the FastAPI book in this event.",
                "tags": ["Book", "FastAPI"],
                "location": "Google Meet"
            }
        }
    }


class EventUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    tags: list[str] | None = None
    location: str | None = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "FastAPI Book Launch",
                "description": "We will be discussing the contents of the FastAPI book in this event.",
                "tags": ["Book", "FastAPI"],
                "location": "Google Meet"
            }
        }
    }
