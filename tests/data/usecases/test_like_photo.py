from src.data.usecases import LikePhoto
from tests.data.mocks.photo_repository_spy import PhotoRepositorySpy


def test_should_like_photo():
    photo_repository_spy = PhotoRepositorySpy()
    sut = LikePhoto(photo_repository_spy)

    user_id = "0"
    photo_id = "0"

    sut.like(user_id, photo_id)

    assert photo_repository_spy.likes == [user_id]
