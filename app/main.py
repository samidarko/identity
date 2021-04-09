import os
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from tortoise.contrib.fastapi import register_tortoise

from callbacks import *
from models import *

DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://localhost/identity")
SECRET = os.environ.get("SECRET", "SECRET")


app = FastAPI(
    title="Identity",
    description="A micro-service to manage users and authentication",
    version="0.1.0",
)
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
)


jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="/auth/jwt/login"
)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(
        SECRET, after_verification_request=after_verification_request
    ),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
