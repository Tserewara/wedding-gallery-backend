from flask import request
from flask.views import MethodView

from src.data.usecases import LikePhoto
from src.main.factories.infra.mongo_photo_repository_factory import (
    mongo_photo_repository_factory,
)

like_photo = LikePhoto(mongo_photo_repository_factory())


class LikePhotoController(MethodView):
    def post(self):

        like_photo.like(
            user_id=request.json.get("user_id"), photo_id=request.json.get("photo_id")
        )

        return "like", 200
