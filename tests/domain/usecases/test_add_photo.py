from src.domain.models import photo_model
from src.domain.usecases import add_photo


def test_should_add_photo_with_correct_params():
    image_address = "any_image_address"
    user_id = "any_user_id"
    result = add_photo(image_address=image_address, user_id=user_id)
    assert result == photo_model.PhotoModel(
        image_address=image_address, user_id=user_id
    )
