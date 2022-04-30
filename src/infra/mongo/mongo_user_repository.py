from bson import ObjectId
from pymongo.database import Database
from pymongo.collection import Collection

from src.domain.models.user_model import UserModel
from src.data.protocols import AbstractUserRepository


class MongoUserRepository(AbstractUserRepository):
    def __init__(self, mongo_client, database_name, collection_name) -> None:
        self._mongo_client = mongo_client
        self._database: Database = self._mongo_client[database_name]
        self._collection: Collection = self._database[collection_name]

    def add(self, user: UserModel):
        self._collection.insert_one(
            {
                "name": user.name,
                "email": user.email,
                "is_admin": user.is_admin,
                "password": user.password,
            }
        )

    def find_user_by_id(self, user_id):
        return self._collection.find_one({"_id": ObjectId(user_id)})

    def find_user_by_email(self, email):
        return self._collection.find_one({"email": email})
