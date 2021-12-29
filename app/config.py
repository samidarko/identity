from environs import Env

env = Env()

DATABASE_URL = env("DATABASE_URL", "postgres://localhost/identity")
SECRET = env("SECRET", "SECRET")
JWT_LIFETIME = env.int("JWT_LIFETIME", 3600)
MIN_LEN_PWD = env.int("MIN_LEN_PWD", 8)
TOKEN_AUDIENCE = env.list("TOKEN_AUDIENCE", ["fastapi-users:auth"])
# log_level = env.log_level("LOG_LEVEL")

CORS_ALLOW_ORIGINS = env.list("CORS_ALLOW_ORIGINS", [])
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS", True)
CORS_ALLOW_METHODS = env.list("CORS_ALLOW_METHODS", ["*"])
CORS_ALLOW_HEADERS = env.list("CORS_ALLOW_HEADERS", ["*"])

ROUTER_AUTH_INCLUDE = env.bool("ROUTER_AUTH_INCLUDE", True)
ROUTER_AUTH_INCLUDE_IN_SCHEMA = env.bool("ROUTER_AUTH_INCLUDE_IN_SCHEMA", True)
ROUTER_AUTH_PREFIX = env("ROUTER_AUTH_PREFIX", "/auth/jwt")
ROUTER_AUTH_TAGS = env.list("ROUTER_AUTH_TAGS", ["auth"])
ROUTER_AUTH_REQUIRES_VERIFICATION = env.bool("ROUTER_AUTH_REQUIRES_VERIFICATION", False)

ROUTER_REGISTER_INCLUDE = env.bool("ROUTER_REGISTER_INCLUDE", True)
ROUTER_REGISTER_INCLUDE_IN_SCHEMA = env.bool("ROUTER_REGISTER_INCLUDE_IN_SCHEMA", True)
ROUTER_REGISTER_PREFIX = env("ROUTER_REGISTER_PREFIX", "/auth")
ROUTER_REGISTER_TAGS = env.list("ROUTER_REGISTER_TAGS", ["auth"])

ROUTER_RESET_PASSWORD_INCLUDE = env.bool("ROUTER_RESET_PASSWORD_INCLUDE", True)
ROUTER_RESET_PASSWORD_INCLUDE_IN_SCHEMA = env.bool(
    "ROUTER_RESET_PASSWORD_INCLUDE_IN_SCHEMA", True
)
ROUTER_RESET_PASSWORD_PREFIX = env("ROUTER_RESET_PASSWORD_PREFIX", "/auth")
ROUTER_RESET_PASSWORD_TAGS = env.list("ROUTER_RESET_PASSWORD_TAGS", ["auth"])

ROUTER_VERIFY_INCLUDE = env.bool("ROUTER_VERIFY_INCLUDE", True)
ROUTER_VERIFY_INCLUDE_IN_SCHEMA = env.bool("ROUTER_VERIFY_INCLUDE_IN_SCHEMA", True)
ROUTER_VERIFY_PREFIX = env("ROUTER_REGISTER_PREFIX", "/auth")
ROUTER_VERIFY_TAGS = env.list("ROUTER_REGISTER_TAGS", ["auth"])

ROUTER_USERS_INCLUDE = env.bool("ROUTER_USERS_INCLUDE", True)
ROUTER_USERS_INCLUDE_IN_SCHEMA = env.bool("ROUTER_USERS_INCLUDE_IN_SCHEMA", True)
ROUTER_USERS_PREFIX = env("ROUTER_USERS_PREFIX", "/users")
ROUTER_USERS_TAGS = env.list("ROUTER_USERS_TAGS", ["users"])
ROUTER_USERS_REQUIRES_VERIFICATION = env.bool(
    "ROUTER_USERS_REQUIRES_VERIFICATION", False
)
