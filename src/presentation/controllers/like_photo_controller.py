from flask import request
from flask.views import MethodView

from src.main.factories.domain.usecases.like_photo_factory import like_photo_factory


like_photo = like_photo_factory()


class LikePhotoController(MethodView):
    def post(self):

        like_photo.like(
            user_id=request.json.get("user_id"), photo_id=request.json.get("photo_id")
        )

        return ("", 204)
