from flask import jsonify, request
from flask.views import MethodView

from src.main.factories.infra.mongo_photo_repository_factory import (
    mongo_photo_repository_factory,
)
from src.main.factories.infra.mongo_user_repository_factory import (
    mongo_user_repository_factory,
)

from src.data.usecases import ApprovePhoto


approve_photo = ApprovePhoto(
    mongo_photo_repository_factory(), mongo_user_repository_factory()
)


class ApprovePhotoController(MethodView):
    def patch(self):

        approve_photo.approve(
            user_id=request.json.get("user_id"), photo_id=request.json.get("photo_id")
        )

        return jsonify(msg="photo approved"), 200
