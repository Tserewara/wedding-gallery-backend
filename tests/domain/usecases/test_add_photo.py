from src.domain.usecases import add_photo
from tests.data.photo_repository_spy import PhotoRepositorySpy
from tests.data.photo_uploader_spy import PhotoUploaderSpy


def test_should_call_photo_uploader_with_correct_params():
    photo_uploader_spy = PhotoUploaderSpy()
    photo_repository_spy = PhotoRepositorySpy()

    file = "any_file"
    filename = "any_file_name"
    user_id = "any_user_id"

    add_photo(user_id, file, filename, photo_uploader_spy, photo_repository_spy)

    assert photo_uploader_spy.file == file
    assert photo_uploader_spy.filename == filename


def test_should_add_photo_information_to_repository():
    photo_uploader_spy = PhotoUploaderSpy()
    photo_repository_spy = PhotoRepositorySpy()

    user_id = "any_user_id"
    filename = "any_file_name"
    file = "any_file"

    add_photo(user_id, file, filename, photo_uploader_spy, photo_repository_spy)

    assert len(photo_repository_spy.photos) == 1
