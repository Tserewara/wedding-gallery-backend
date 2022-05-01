from src.data.usecases import ApprovePhoto
from src.main.factories.infra import (
    mongo_photo_repository_factory,
    mongo_user_repository_factory,
)


def approve_photo_factory():
    return ApprovePhoto(
        mongo_photo_repository_factory(), mongo_user_repository_factory()
    )
