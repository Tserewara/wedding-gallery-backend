from flask import jsonify, request
from flask.views import MethodView

from src.main.factories.domain.usecases.add_photo_factory import add_photo_factory
from src.domain.errors import MissingParamError
from src.data.errors import UploadError


add_photo = add_photo_factory()


class AddPhotoController(MethodView):
    def post(self):

        try:

            file = request.files.get("photo")
            filename = file.filename if file else None

            add_photo.add(
                user_id=request.form.get("user_id"), filename=filename, file=file
            )

            return jsonify(msg="photo added successfully"), 201

        except (UploadError, MissingParamError) as e:
            status_code = 500 if type(e) == "UploadError" else 400
            return jsonify(msg=str(e)), status_code
