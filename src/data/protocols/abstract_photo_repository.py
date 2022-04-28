import abc

from src.domain.models import PhotoModel


class AbstractPhotoRepository(abc.ABC):
    def add(self, photo: PhotoModel):
        self.photos.append(photo)
