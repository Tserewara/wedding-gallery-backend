from src.data.protocols import AbstractPhotoUploader


def add_photo(user_id: str, file, filename: str, photo_uploader: AbstractPhotoUploader):
    photo_uploader.upload(file, filename)
