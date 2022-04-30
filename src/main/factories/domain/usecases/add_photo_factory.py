from src.main.factories.infra.s3_photo_uploader_factory import s3_photo_uploader_factory
from src.main.factories.infra.mongo_photo_repository_factory import (
    mongo_photo_repository_factory,
)
from src.data.usecases import AddPhoto


def add_photo_factory():
    return AddPhoto(s3_photo_uploader_factory(), mongo_photo_repository_factory())
