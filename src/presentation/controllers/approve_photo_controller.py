from flask import jsonify, request
from flask.views import MethodView

from src.main.factories.domain.usecases.approve_photo_factory import (
    approve_photo_factory,
)
from src.domain.errors.photo_not_found_error import PhotoNotFoundError
from src.domain.errors.user_not_found_error import UserNotFoundError


approve_photo = approve_photo_factory()


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
