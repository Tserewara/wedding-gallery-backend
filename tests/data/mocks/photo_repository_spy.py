from src.data.protocols import AbstractPhotoRepository
from src.domain.models import PhotoModel


class PhotoRepositorySpy(AbstractPhotoRepository):
    def __init__(self) -> None:
        self.photos = []

    def add(self, photo: PhotoModel):
        self.photos.append(photo)
