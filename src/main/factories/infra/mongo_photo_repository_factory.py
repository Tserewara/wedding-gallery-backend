from src.main.factories.infra import mongo_client_factory
from src.infra.mongo import MongoPhotoRepository


def mongo_photo_repository_factory():
    client, database_name = mongo_client_factory()
    return MongoPhotoRepository(client, database_name, "photos")
