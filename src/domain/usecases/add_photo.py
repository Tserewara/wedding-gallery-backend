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

    photo = PhotoModel(user_id, "any_image_address")

    photo_repository.add(photo)
