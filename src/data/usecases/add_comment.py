from src.domain.errors.missing_param_error import MissingParamError
from src.data.protocols import AbstractPhotoRepository
from src.domain.usecases import AbstractAddComment


class AddComment(AbstractAddComment):
    def __init__(self, photo_repository: AbstractPhotoRepository) -> None:
        super().__init__(photo_repository)

    def comment(self, username, photo_id, text):
        if not text:
            raise MissingParamError("You must add some content")
        self.photo_repository.update_photo(
            photo_id, "comments", {"username": username, "text": text}
        )

        return {"username": username, "photo_id": photo_id, "text": text}
