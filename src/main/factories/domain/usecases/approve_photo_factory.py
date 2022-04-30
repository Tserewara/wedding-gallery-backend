from src.data.usecases.approve_photo import ApprovePhoto
from src.main.factories.infra.mongo_photo_repository_factory import (
    mongo_photo_repository_factory,
)
from src.main.factories.infra.mongo_user_repository_factory import (
    mongo_user_repository_factory,
)


def approve_photo_factory():
    return ApprovePhoto(
        mongo_photo_repository_factory(), mongo_user_repository_factory()
    )
