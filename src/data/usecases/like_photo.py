from src.data.protocols import AbstractPhotoRepository
from src.domain.usecases import AbstractLikePhoto


class LikePhoto(AbstractLikePhoto):
    def __init__(self, photo_repository: AbstractPhotoRepository) -> None:
        super().__init__(photo_repository)

    def like(self, user_id, photo_id):
        self.photo_repository.update_photo(photo_id, "likes", user_id)
