import abc
from typing import Any

from src.data.protocols import AbstractPhotoUploader, AbstractPhotoRepository


class AbstractAddPhoto(abc.ABC):
    def __init__(
        self,
        photo_uploader: AbstractPhotoUploader,
        photo_repository: AbstractPhotoRepository,
    ) -> None:
        super().__init__()
        self.photo_uploader = photo_uploader
        self.photo_repository = photo_repository

    @abc.abstractmethod
    def add(
        self,
        user_id: str,
        filename: str,
        file: Any,
    ):
        raise NotImplementedError
