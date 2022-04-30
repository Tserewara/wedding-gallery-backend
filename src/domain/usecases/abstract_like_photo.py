import abc

from src.data.protocols import AbstractPhotoRepository


class AbstractLikePhoto(abc.ABC):
    def __init__(self, photo_repository: AbstractPhotoRepository) -> None:
        self.photo_repository = photo_repository

    @abc.abstractmethod
    def like(self, user_id, photo_id):
        raise NotImplementedError
