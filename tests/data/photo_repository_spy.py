from src.domain.models import PhotoModel


class PhotoRepositorySpy:
    def __init__(self) -> None:
        self.photos = []

    def add(self, photo: PhotoModel):
        self.photos.append(photo)
