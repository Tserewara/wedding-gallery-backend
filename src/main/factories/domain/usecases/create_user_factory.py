from src.infra.mongo.mongo_user_repository import MongoUserRepository
from src.data.usecases import CreateUser
from src.infra.passlib.passlib_password_encryptor import PasslibPasswordEncryptor

from src.infra.mongo.mongo_client import client


def create_user_factory():
    user_repository = MongoUserRepository(client, "friends-gallery", "users")

    password_encryptor = PasslibPasswordEncryptor()

    return CreateUser(user_repository, password_encryptor)
