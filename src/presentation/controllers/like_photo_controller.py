from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from src.main.factories.domain.usecases import like_photo_factory


like_photo = like_photo_factory()


class LikePhotoController(MethodView):
    @jwt_required()
    def post(self):

        like_photo.like(
            user_id=request.json.get("user_id"), photo_id=request.json.get("photo_id")
        )

        return ("", 204)
