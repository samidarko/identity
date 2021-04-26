from environs import Env
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from tortoise.contrib.fastapi import register_tortoise

from callbacks import *
from models import *

env = Env()

DATABASE_URL = env("DATABASE_URL", "postgres://localhost/identity")
SECRET = env("SECRET", "SECRET")
JWT_LIFETIME = env.int("JWT_LIFETIME", 3600)
# log_level = env.log_level("LOG_LEVEL")

CORS_ALLOW_ORIGINS = env.list("CORS_ALLOW_ORIGINS", [])
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS ", True)
CORS_ALLOW_METHODS = env.list("CORS_ALLOW_METHODS", ["*"])
CORS_ALLOW_HEADERS = env.list("CORS_ALLOW_HEADERS", ["*"])

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

app = FastAPI(
    title="Identity",
    description="A micro-service to manage users and authentication",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=CORS_ALLOW_CREDENTIALS,
    allow_methods=CORS_ALLOW_METHODS,
    allow_headers=CORS_ALLOW_HEADERS,
)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=False,
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
