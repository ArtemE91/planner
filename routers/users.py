from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from database.objects import Database
from models.users import User, TokenResponse

user_router = APIRouter(tags=["User"])
user_database = Database(User)
hash_password = HashPassword()


@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = await User.find_one(User.username == user.username)
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            "access_token": access_token, "token_type": "Bearer"
        }

@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already."
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.create(user)
    return {"message": "User created successfully"}

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
