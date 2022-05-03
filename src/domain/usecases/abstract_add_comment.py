import abc

from src.data.protocols import AbstractPhotoRepository


class AbstractAddComment(abc.ABC):
    def __init__(self, photo_repository: AbstractPhotoRepository) -> None:
        self.photo_repository = photo_repository

    @abc.abstractmethod
    def comment(self, username, photo_id, text):
        raise NotImplementedError
