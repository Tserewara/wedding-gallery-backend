from src.main.factories.infra.mongo_client_factory import mongo_client_factory
from src.infra.mongo.mongo_photo_repository import MongoPhotoRepository


def mongo_photo_repository_factory():
    client, database_name = mongo_client_factory()
    return MongoPhotoRepository(client, database_name, "photos")
