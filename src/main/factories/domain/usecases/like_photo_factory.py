from src.data.usecases import LikePhoto
from src.main.factories.infra import mongo_photo_repository_factory


def like_photo_factory():
    return LikePhoto(mongo_photo_repository_factory())
