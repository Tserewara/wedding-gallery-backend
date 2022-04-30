from src.infra.mongo.mongo_client import client
from src.infra.mongo.mongo_user_repository import MongoUserRepository


def mongo_user_repository_factory():
    return MongoUserRepository(client, "friends-gallery", "users")
