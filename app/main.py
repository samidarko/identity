from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from config import *
from users import fastapi_users, jwt_authentication


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

if ROUTER_AUTH_INCLUDE:
    app.include_router(
        fastapi_users.get_auth_router(
            jwt_authentication, requires_verification=ROUTER_AUTH_REQUIRES_VERIFICATION
        ),
        prefix=ROUTER_AUTH_PREFIX,
        tags=ROUTER_AUTH_TAGS,
        include_in_schema=ROUTER_AUTH_INCLUDE_IN_SCHEMA,
    )

if ROUTER_REGISTER_INCLUDE:
    app.include_router(
        fastapi_users.get_register_router(),
        prefix=ROUTER_REGISTER_PREFIX,
        tags=ROUTER_REGISTER_TAGS,
        include_in_schema=ROUTER_REGISTER_INCLUDE_IN_SCHEMA,
    )

if ROUTER_RESET_PASSWORD_INCLUDE:
    app.include_router(
        fastapi_users.get_reset_password_router(),
        prefix=ROUTER_RESET_PASSWORD_PREFIX,
        tags=ROUTER_RESET_PASSWORD_TAGS,
        include_in_schema=ROUTER_RESET_PASSWORD_INCLUDE_IN_SCHEMA,
    )

if ROUTER_VERIFY_INCLUDE:
    app.include_router(
        fastapi_users.get_verify_router(),
        prefix=ROUTER_VERIFY_PREFIX,
        tags=ROUTER_VERIFY_TAGS,
        include_in_schema=ROUTER_VERIFY_INCLUDE_IN_SCHEMA,
    )

if ROUTER_USERS_INCLUDE:
    app.include_router(
        fastapi_users.get_users_router(
            requires_verification=ROUTER_USERS_REQUIRES_VERIFICATION
        ),
        prefix=ROUTER_USERS_PREFIX,
        tags=ROUTER_USERS_TAGS,
        include_in_schema=ROUTER_USERS_INCLUDE_IN_SCHEMA,
    )

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=False,
)
