import pytest

from src.domain.models import UserModel
from src.domain.errors import PermissionDeniedError
from src.domain.models.photo_model import PhotoModel

from src.data.protocols import AbstractPhotoRepository
from src.domain.usecases import AbstractApprovePhoto
from tests.data.mocks.photo_repository_spy import PhotoRepositorySpy
from tests.data.mocks.user_repository_spy import (
    AbstractUserRepository,
    UserRepositorySpy,
)
from tests.data.usecases.test_create_user import mock_create_user_params


class ApprovePhoto(AbstractApprovePhoto):
    def __init__(
        self,
        photo_repository: AbstractPhotoRepository,
        user_repository: AbstractUserRepository,
    ) -> None:
        super().__init__(photo_repository, user_repository)

    def approve(self, user_id, photo_id):
        user: UserModel = self.user_repository.find_user_by_id(user_id)
        if not user.is_admin:
            raise PermissionDeniedError("You don't have permission to approve photos")


def test_should_raise_permission_denied_error_when_not_admin():
    photo_repository_spy = PhotoRepositorySpy()
    user_repository_spy = UserRepositorySpy()

    sut = ApprovePhoto(photo_repository_spy, user_repository_spy)

    photo_id = "0"
    user_id = "0"

    name, email, password, _ = mock_create_user_params()

    user = UserModel(name, email, password)

    user_repository_spy.add(user)

    with pytest.raises(PermissionDeniedError):
        sut.approve(user_id, photo_id)
