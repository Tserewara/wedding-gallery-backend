from src.domain.models import PhotoModel
from src.data.protocols import AbstractPhotoUploader, AbstractPhotoRepository


def add_photo(
    user_id: str,
    file,
    filename: str,
    photo_uploader: AbstractPhotoUploader,
    photo_repository: AbstractPhotoRepository,
):
    photo_uploader.upload(file, filename)

    photo = PhotoModel(user_id, "")

    photo_repository.add(photo)
