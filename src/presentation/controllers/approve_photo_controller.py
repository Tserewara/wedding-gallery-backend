from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from src.main.factories.domain.usecases import approve_photo_factory
from src.domain.errors import PhotoNotFoundError
from src.domain.errors import UserNotFoundError


approve_photo = approve_photo_factory()


class ApprovePhotoController(MethodView):
    @jwt_required()
    def patch(self):

        try:

            approve_photo.approve(
                user_id=request.json.get("user_id"),
                photo_id=request.json.get("photo_id"),
            )

            return jsonify(msg="photo approved"), 200

        except (UserNotFoundError, PhotoNotFoundError) as e:
            return jsonify(msg=str(e)), 404
