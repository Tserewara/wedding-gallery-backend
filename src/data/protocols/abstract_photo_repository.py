import abc
from typing import Any

from src.domain.models import PhotoModel


class AbstractPhotoRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, photo: PhotoModel):
        raise NotImplementedError

    @abc.abstractmethod
    def find_photo_by_id(self, photo_id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def update_photo(self, fieldname: str, value=Any):
        raise NotImplementedError
