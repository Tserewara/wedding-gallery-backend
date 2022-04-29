import pytest

from src.domain.models import PhotoModel


from src.data.usecases import ApprovePhoto
from src.domain.models import UserModel
from src.domain.errors import (
    PermissionDeniedError,
    PhotoNotFoundError,
    UserNotFoundError,
)
from tests.data.mocks.photo_repository_spy import PhotoRepositorySpy
from tests.data.mocks.user_repository_spy import UserRepositorySpy
from tests.domain.models.mocks.mock_user_params import mock_user_params


def make_sut():
    photo_repository_spy = PhotoRepositorySpy()
    user_repository_spy = UserRepositorySpy()

    sut = ApprovePhoto(photo_repository_spy, user_repository_spy)

    return sut, photo_repository_spy, user_repository_spy


def mock_user_model(is_admin: bool = False):
    name, email, password, _ = mock_user_params()
    return UserModel(name, email, password, is_admin=is_admin)


def mock_photo_model(user_id: str = "0"):
    image_address = "any_image_address"
    return PhotoModel(user_id, image_address)


def test_should_raise_user_not_found_error_if_user_does_not_exist():
    sut, _, _ = make_sut()

    photo_id = "0"
    user_id = "0"

    with pytest.raises(UserNotFoundError):
        sut.approve(user_id, photo_id)


def test_should_raise_photo_not_found_error_if_photo_does_not_exist():
    sut, _, user_repository_spy = make_sut()

    user = mock_user_model()

    user_repository_spy.add(user)

    photo_id = "0"
    user_id = "0"

    with pytest.raises(PhotoNotFoundError):
        sut.approve(user_id, photo_id)


def test_should_raise_permission_denied_error_when_not_admin():
    sut, photo_repository_spy, user_repository_spy = make_sut()

    user = mock_user_model()
    user_repository_spy.add(user)

    user_id = "0"
    photo_id = "0"

    photo = mock_photo_model(user_id)

    photo_repository_spy.add(photo)

    with pytest.raises(PermissionDeniedError):
        sut.approve(user_id, photo_id)


def test_should_approve_photo_if_user_is_admin():
    sut, photo_repository_spy, user_repository_spy = make_sut()

    user = mock_user_model(is_admin=True)
    user_repository_spy.add(user)

    photo_id = "0"
    user_id = "0"

    photo = mock_photo_model()
    photo_repository_spy.add(photo)

    sut.approve(user_id, photo_id)

    assert photo.is_approved
