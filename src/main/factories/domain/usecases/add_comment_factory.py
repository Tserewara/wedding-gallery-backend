from src.data.usecases import AddComment
from src.main.factories.infra.mongo_photo_repository_factory import (
    mongo_photo_repository_factory,
)


def add_comment_factory():
    return AddComment(mongo_photo_repository_factory())
