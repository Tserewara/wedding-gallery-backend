from src.domain.errors import MissingParamError
from src.domain.models import PhotoModel
from src.domain.usecases import AbstractAddPhoto
from src.data.protocols import AbstractPhotoUploader, AbstractPhotoRepository
from src.data.errors import UploadError


class AddPhoto(AbstractAddPhoto):
    def __init__(
        self,
        photo_uploader: AbstractPhotoUploader,
        photo_repository: AbstractPhotoRepository,
    ) -> None:
        super().__init__(photo_uploader, photo_repository)

    def add(self, user_id: str, filename: str, file):

        if None in [filename, file, user_id]:
            raise MissingParamError(
                "Parameter missing. Make sure to provide user_id, filename and file"
            )

        result = self.photo_uploader.upload(file, filename)

        if result["error"]:
            raise UploadError("An error occurred while uploading this photo.")

        photo = PhotoModel(user_id, result["message"])

        self.photo_repository.add(photo)

        return photo
