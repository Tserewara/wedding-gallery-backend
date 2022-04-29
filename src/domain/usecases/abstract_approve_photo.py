import abc

from src.data.protocols import AbstractPhotoRepository, AbstractUserRepository


class AbstractApprovePhoto(abc.ABC):
    def __init__(
        self,
        photo_repository: AbstractPhotoRepository,
        user_repository: AbstractUserRepository,
    ) -> None:
        self.photo_repository = photo_repository
        self.user_repository = user_repository

    @abc.abstractmethod
    def approve(self, photo_id, user_id):
        raise NotImplementedError
