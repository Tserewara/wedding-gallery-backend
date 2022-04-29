from typing import Tuple
import pytest

from src.data.usecases import AddPhoto
from src.data.errors import UploadError

from src.domain.models import PhotoModel

from tests.data.mocks.photo_repository_spy import PhotoRepositorySpy
from tests.data.mocks.photo_uploader_spy import PhotoUploaderSpy


def make_sut() -> Tuple[AddPhoto, PhotoUploaderSpy, PhotoRepositorySpy]:
    photo_uploader_spy = PhotoUploaderSpy()
    photo_repository_spy = PhotoRepositorySpy()
    sut = AddPhoto(photo_uploader_spy, photo_repository_spy)
    return sut, photo_uploader_spy, photo_repository_spy


def mock_add_photo_params(
    file: str = "any_file", filename: str = "any_filename", user_id: str = "any_user_id"
):
    return file, filename, user_id


def test_should_call_photo_uploader_with_correct_params():
    sut, photo_uploader_spy, _ = make_sut()

    file, filename, user_id = mock_add_photo_params()

    sut.add(user_id, filename, file)

    assert photo_uploader_spy.file == file
    assert photo_uploader_spy.filename == filename


def test_should_add_photo_information_to_repository():
    sut, _, photo_repository_spy = make_sut()

    file, filename, user_id = mock_add_photo_params()

    sut.add(user_id, filename, file)

    assert len(photo_repository_spy.photos) == 1


def test_should_return_photo_model_if_upload_succeeds():
    sut, _, _ = make_sut()

    file, filename, user_id = mock_add_photo_params()

    photo_model = PhotoModel(user_id, filename)

    result = sut.add(user_id, filename, file)

    assert result == photo_model


def test_should_raise_error_if_upload_fails():
    sut, photo_uploader_spy, _ = make_sut()

    photo_uploader_spy.result["error"] = UploadError

    file, filename, user_id = mock_add_photo_params()

    with pytest.raises(UploadError):
        sut.add(user_id, filename, file)