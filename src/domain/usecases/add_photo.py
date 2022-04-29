from src.data.errors import UploadError
from src.domain.models import PhotoModel
from src.data.protocols import AbstractPhotoUploader, AbstractPhotoRepository


def add_photo(
    user_id: str,
    file,
    filename: str,
    photo_uploader: AbstractPhotoUploader,
    photo_repository: AbstractPhotoRepository,
):
    result = photo_uploader.upload(file, filename)

    if result == "error":
        raise UploadError("An error occurred while uploading this photo.")

    photo = PhotoModel(user_id, result)

    photo_repository.add(photo)

    return photo
