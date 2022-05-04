from bson import ObjectId
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
        result = self._collection.insert_one(
            {
                "image_address": photo.image_address,
                "user_id": photo.user_id,
                "username": photo.username,
                "comments": [],
                "likes": [],
                "is_approved": photo.is_approved,
            }
        )
        return result.inserted_id

    def find_photo_by_id(self, photo_id: str) -> PhotoModel:
        return self._collection.find_one({"_id": ObjectId(photo_id)})

    def update_photo(self, photo_id: str, fieldname: str, value=...):
        action = {"is_approved": "$set", "likes": "$push", "comments": "$push"}

        self._collection.update_one(
            {"_id": ObjectId(photo_id)}, {action[fieldname]: {fieldname: value}}
        )

    def list_photos(self, skips, per_page, filter):
        return self._collection.find(filter).skip(skips).limit(per_page)
