import pytest
from httpx import AsyncClient

from models.events import Event


@pytest.mark.asyncio
async def test_get_events(test_async_client: AsyncClient, mock_event: Event) -> None:
    response = await test_async_client.get("/events/")
    assert response.status_code == 200
    assert response.json()[0]["_id"] == str(mock_event.id)


@pytest.mark.asyncio
async def test_get_event(test_async_client: AsyncClient, mock_event: Event) -> None:
    url = f"/events/{str(mock_event.id)}"
    response = await test_async_client.get(url)
    assert response.status_code == 200
    assert response.json()["creator"] == mock_event.creator
    assert response.json()["_id"] == str(mock_event.id)


@pytest.mark.asyncio
async def test_post_event(test_async_client: AsyncClient, access_token: str) -> None:
    payload = {
        "title": "FastAPI Book Launch",
        "description": "Description",
        "tags": ["python", "fastapi"],
        "location": "Google Meet"
    }

    headers = {
        "Content-Type": "application/json", "Authorization": f"Bearer {access_token}"
    }

    success_response = {
        "message": "Event created successfully"
    }

    response = await test_async_client.post("/events/", json=payload, headers=headers)

    assert response.status_code == 200
    assert response.json() == success_response


@pytest.mark.asyncio
async def test_get_events_count(test_async_client: AsyncClient) -> None:
    response = await test_async_client.get("/events/")
    events = response.json()
    assert response.status_code == 200
    assert len(events) == 2


@pytest.mark.asyncio
async def test_update_event(test_async_client: AsyncClient, mock_event: Event, access_token: str) -> None:
    test_payload = {
        "title": "Updated FastAPI event"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    url = f"/events/{str(mock_event.id)}"
    response = await test_async_client.put(url, json=test_payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated FastAPI event"


@pytest.mark.asyncio
async def test_delete_event(test_async_client: AsyncClient, mock_event: Event, access_token: str) -> None:
    success_response = {
        "message": "Event deleted successfully."
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    url = f"/events/{mock_event.id}"
    response = await test_async_client.delete(url, headers=headers)
    assert response.status_code == 200
    assert response.json() == success_response


@pytest.mark.asyncio
async def test_get_event_again(test_async_client: AsyncClient, mock_event: Event) -> None:
    url = f"/events/{str(mock_event.id)}"
    response = await test_async_client.get(url)
    assert response.status_code == 404
