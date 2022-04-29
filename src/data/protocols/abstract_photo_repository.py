import abc

from src.domain.models import PhotoModel


class AbstractPhotoRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, photo: PhotoModel):
        raise NotImplementedError

    @abc.abstractmethod
    def find_photo_by_id(self, photo_id: str):
        raise NotImplementedError
