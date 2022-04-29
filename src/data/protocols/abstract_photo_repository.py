import abc

from src.domain.models import PhotoModel


class AbstractPhotoRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, photo: PhotoModel):
        raise NotImplementedError
