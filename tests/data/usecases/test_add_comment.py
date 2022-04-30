from src.data.usecases import AddComment
from tests.data.mocks.photo_repository_spy import PhotoRepositorySpy


def test_should_like_photo():
    photo_repository_spy = PhotoRepositorySpy()
    sut = AddComment(photo_repository_spy)

    user_id = "0"
    photo_id = "0"
    text = "A comment"

    sut.comment(user_id, photo_id, text)

    assert photo_repository_spy.comments == [{user_id: text}]
