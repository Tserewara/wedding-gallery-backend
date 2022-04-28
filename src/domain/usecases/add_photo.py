from src.domain.models import PhotoModel


def add_photo(image_address: str, user_id: str):
    return PhotoModel(
        image_address=image_address,
        user_id=user_id)