from src.domain.models import PhotoModel


def mock_photo_model(user_id: str = "0") -> PhotoModel:
    return PhotoModel(
        user_id, image_address="any_image_address", username="any_username"
    )
