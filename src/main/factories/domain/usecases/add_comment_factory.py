from src.data.usecases import AddComment
from src.main.factories.infra import mongo_photo_repository_factory


def add_comment_factory():
    return AddComment(mongo_photo_repository_factory())
