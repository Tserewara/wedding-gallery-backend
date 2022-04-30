from src.domain.errors.missing_param_error import MissingParamError
from src.data.protocols import AbstractPhotoRepository
from src.domain.usecases import AbstractAddComment


class AddComment(AbstractAddComment):
    def __init__(self, photo_repository: AbstractPhotoRepository) -> None:
        super().__init__(photo_repository)

    def comment(self, user_id, photo_id, text):
        if text is None:
            raise MissingParamError("You must add some content")
        self.photo_repository.update_photo(photo_id, "comments", {user_id: text})
