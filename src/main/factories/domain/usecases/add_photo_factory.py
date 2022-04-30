from src.infra.s3.s3_photo_uploader import S3PhotoUploader
from src.data.usecases import AddPhoto
from src.main.factories.infra.mongo_user_repository_factory import mongo_client_factory
from src.infra.mongo.mongo_photo_repository import MongoPhotoRepository


def add_photo_factory():
    photo_uploader = S3PhotoUploader()
    photo_repository = MongoPhotoRepository(*mongo_client_factory(), "photos")
    return AddPhoto(photo_uploader, photo_repository)
