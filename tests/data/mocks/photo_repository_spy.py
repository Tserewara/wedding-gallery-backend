from typing import Any
from src.data.protocols import AbstractPhotoRepository
from src.domain.models import PhotoModel


class PhotoRepositorySpy(AbstractPhotoRepository):
    def __init__(self) -> None:
        self.photos = []

    def add(self, photo: PhotoModel):
        self.photos.append(photo)

    def find_photo_by_id(self, photo_id: str):
        if not self.photos:
            return None
        return self.photos[int(photo_id)]

    def update_photo(self, photo_id: str, fieldname: str, value=Any):
        photo = self.find_photo_by_id(photo_id)
        photo.is_approved = value
