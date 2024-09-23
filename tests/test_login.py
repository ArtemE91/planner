import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_sign_new_user(test_async_client: AsyncClient) -> None:
    payload = {
        "email": "testuser@packt.com", "password": "testpassword", "username": "testuser@packt.com"
    }
    headers = {
        "accept": "application/json", "Content-Type": "application/json"
    }
    test_response = {
        "message": "User created successfully"
    }
    response = await test_async_client.post("/users/signup", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_sign_user_in(test_async_client: AsyncClient) -> None:
    payload = {
        "username": "testuser@packt.com",
        "password": "testpassword"
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = await test_async_client.post("/users/signin", data=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"


@pytest.mark.asyncio
async def test_sign_user_in_not_found(test_async_client: AsyncClient) -> None:
    payload = {
        "username": "notfound@packt.com",
        "password": "testpassword"
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = await test_async_client.post("/users/signin", data=payload, headers=headers)
    assert response.status_code == 404
