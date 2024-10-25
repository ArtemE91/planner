from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status

from database.objects import Database
from models.users import User

user_router = APIRouter(tags=["User"])
user_database = Database(User)


@user_router.get("/", response_model=list[User])
async def retrieve_all_users() -> list[User]:
    users = await user_database.get_all()
    return users


@user_router.get("/{user_id}", response_model=User)
async def retrieve_user(user_id: PydanticObjectId) -> User:
    user = await user_database.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied ID does not exist"
        )
    return user


@user_router.post("/")
async def create_user(body: User) -> dict:
    await user_database.create(body)
    return {"message": "User created successfully"}