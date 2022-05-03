from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from src.main.factories.infra import mongo_user_repository_factory
from src.main.factories.domain.usecases import add_photo_factory
from src.domain.errors import MissingParamError
from src.data.errors import UploadError


add_photo = add_photo_factory()
user_repository = mongo_user_repository_factory()


class AddPhotoController(MethodView):
    @jwt_required()
    def post(self):

        try:

            file = request.files.get("photo")
            filename = file.filename if file else None
            user_id = request.form.get("user_id")

            username = user_repository.find_user_by_id(user_id)["name"]

            add_photo.add(
                user_id=user_id, username=username, filename=filename, file=file
            )

            return jsonify(msg="photo added successfully"), 201

        except UploadError as e:
            return jsonify(msg=str(e)), 500

        except MissingParamError as e:
            return jsonify(msg=str(e)), 400
