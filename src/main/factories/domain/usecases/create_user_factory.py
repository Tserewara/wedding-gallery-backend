from src.main.factories.infra import (
    passlib_password_encryptor_factory,
    mongo_user_repository_factory,
)
from src.data.usecases import CreateUser


def create_user_factory():

    return CreateUser(
        mongo_user_repository_factory(), passlib_password_encryptor_factory()
    )
