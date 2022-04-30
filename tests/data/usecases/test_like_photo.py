from src.data.protocols import AbstractPhotoRepository
from src.domain.usecases import AbstractLikePhoto
from tests.data.mocks.photo_repository_spy import PhotoRepositorySpy


class LikePhoto(AbstractLikePhoto):
    def __init__(self, photo_repository: AbstractPhotoRepository) -> None:
        super().__init__(photo_repository)

    def like(self, user_id, photo_id):
        self.photo_repository.update_photo(photo_id, "likes", user_id)


def test_should_like_photo():
    photo_repository_spy = PhotoRepositorySpy()
    sut = LikePhoto(photo_repository_spy)

    user_id = "0"
    photo_id = "0"

    sut.like(user_id, photo_id)

    assert photo_repository_spy.likes == [user_id]
