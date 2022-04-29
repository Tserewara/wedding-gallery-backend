from pymongo.collection import Collection
from pymongo.database import Database
from src.domain.models import PhotoModel


from src.data.protocols import AbstractPhotoRepository


class MongoPhotoRepository(AbstractPhotoRepository):
    def __init__(self, mongo_client, database_name, collection_name) -> None:
        self._mongo_client = mongo_client
        self._database: Database = self._mongo_client[database_name]
        self._collection: Collection = self._database[collection_name]

    def add(self, photo: PhotoModel) -> None:
        self._collection.insert_one(
            {"image_address": photo.image_address, "user_id": photo.user_id}
        )
