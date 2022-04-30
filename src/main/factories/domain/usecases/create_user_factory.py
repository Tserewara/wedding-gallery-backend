from src.main.factories.infra.mongo_user_repository_factory import (
    mongo_user_repository_factory,
)
from src.data.usecases import CreateUser
from src.infra.passlib.passlib_password_encryptor import PasslibPasswordEncryptor


def create_user_factory():

    password_encryptor = PasslibPasswordEncryptor()

    return CreateUser(mongo_user_repository_factory(), password_encryptor)
