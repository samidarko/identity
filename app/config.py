from environs import Env

env = Env()

DATABASE_URL = env("DATABASE_URL", "postgres://localhost/identity")
SECRET = env("SECRET", "SECRET")
JWT_LIFETIME = env.int("JWT_LIFETIME", 3600)
MIN_LEN_PWD = env.int("MIN_LEN_PWD", 8)
# log_level = env.log_level("LOG_LEVEL")

CORS_ALLOW_ORIGINS = env.list("CORS_ALLOW_ORIGINS", [])
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS ", True)
CORS_ALLOW_METHODS = env.list("CORS_ALLOW_METHODS", ["*"])
CORS_ALLOW_HEADERS = env.list("CORS_ALLOW_HEADERS", ["*"])
