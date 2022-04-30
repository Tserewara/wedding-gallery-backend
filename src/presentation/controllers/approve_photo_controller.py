from flask import jsonify, request
from flask.views import MethodView

from src.domain.errors.photo_not_found_error import PhotoNotFoundError
from src.domain.errors.user_not_found_error import UserNotFoundError
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

        try:

            approve_photo.approve(
                user_id=request.json.get("user_id"),
                photo_id=request.json.get("photo_id"),
            )

            return jsonify(msg="photo approved"), 200

        except (UserNotFoundError, PhotoNotFoundError) as e:
            return jsonify(msg=str(e)), 404
