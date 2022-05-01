from src.main.factories.infra import mongo_client_factory
from src.infra.mongo import MongoUserRepository


def mongo_user_repository_factory():
    client, database_name = mongo_client_factory()
    return MongoUserRepository(client, database_name, "users")
