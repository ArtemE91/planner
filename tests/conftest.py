from beanie import init_beanie
from httpx import AsyncClient

import pytest
from mongomock_motor import AsyncMongoMockClient

from auth.jwt_handler import create_access_token
from main import app
from models.events import Event
from models.users import User


@pytest.fixture(autouse=True, scope="session")
async def mongo_mock():
    client = AsyncMongoMockClient()
    await init_beanie(document_models=[Event, User], database=client.get_database(name="db"))

@pytest.fixture(scope="session")
async def test_async_client():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


@pytest.fixture(scope="module")
async def access_token() -> str:
    return create_access_token("testuser@packt.com")


@pytest.fixture(scope="module")
async def mock_event() -> Event:
    new_event = Event(
        creator="testuser@packt.com",
        title="FastAPI",
        description="Description!",
        tags=["python", "fastapi"],
        location="Google Meet"
    )
    await Event.insert_one(new_event)
    yield new_event

