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

    def add(self, user_id: str, username, filename: str, file):

        if not all([filename, file, user_id, username]):
            raise MissingParamError("Parameter missing")

        result = self.photo_uploader.upload(file, filename)

        if result["error"]:
            raise UploadError("An error occurred while uploading this photo.")

        photo = PhotoModel(user_id, username=username, image_address=result["message"])

        photo_id = self.photo_repository.add(photo)

        return photo, photo_id
