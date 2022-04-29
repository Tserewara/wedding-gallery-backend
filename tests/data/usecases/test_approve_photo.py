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


def test_should_raise_user_not_found_error_if_user_does_not_exist():
    photo_repository_spy = PhotoRepositorySpy()
    user_repository_spy = UserRepositorySpy()

    sut = ApprovePhoto(photo_repository_spy, user_repository_spy)

    photo_id = "0"
    user_id = "0"

    with pytest.raises(UserNotFoundError):
        sut.approve(user_id, photo_id)


def test_should_raise_photo_not_found_error_if_photo_does_not_exist():
    photo_repository_spy = PhotoRepositorySpy()
    user_repository_spy = UserRepositorySpy()

    sut = ApprovePhoto(photo_repository_spy, user_repository_spy)

    name, email, password, _ = mock_user_params()

    user = UserModel(name, email, password, is_admin=True)

    user_repository_spy.add(user)

    photo_id = "0"
    user_id = "0"

    with pytest.raises(PhotoNotFoundError):
        sut.approve(user_id, photo_id)


def test_should_raise_permission_denied_error_when_not_admin():
    photo_repository_spy = PhotoRepositorySpy()
    user_repository_spy = UserRepositorySpy()

    sut = ApprovePhoto(photo_repository_spy, user_repository_spy)

    photo_id = "0"
    user_id = "0"
    image_address = "any_image_address"

    name, email, password, _ = mock_user_params()

    user = UserModel(name, email, password)
    user_repository_spy.add(user)

    photo = PhotoModel(user_id, image_address)
    photo_repository_spy.add(photo)

    with pytest.raises(PermissionDeniedError):
        sut.approve(user_id, photo_id)


def test_should_approve_photo_if_user_is_admin():
    photo_repository_spy = PhotoRepositorySpy()
    user_repository_spy = UserRepositorySpy()

    sut = ApprovePhoto(photo_repository_spy, user_repository_spy)

    name, email, password, _ = mock_user_params()

    user = UserModel(name, email, password, is_admin=True)
    user_repository_spy.add(user)

    photo_id = "0"
    user_id = "0"
    image_address = "any_image_address"

    photo = PhotoModel(user_id, image_address)
    photo_repository_spy.add(photo)

    sut.approve(user_id, photo_id)

    assert photo.is_approved
