import abc

from data.protocols.abstract_photo_repository import AbstractPhotoRepository


class AbstractApprovePhoto(abc.ABC):
    def __init__(self, photo_repository: AbstractPhotoRepository) -> None:
        self.photo_repository = photo_repository

    @abc.abstractmethod
    def approve(self, photo_id, user_id):
        raise NotImplementedError
