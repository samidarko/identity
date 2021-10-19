from fastapi_users.db import TortoiseUserDatabase
from models import UserDB, UserModel


def get_user_db():
    yield TortoiseUserDatabase(UserDB, UserModel)
