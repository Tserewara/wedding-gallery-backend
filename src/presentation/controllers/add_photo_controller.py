from flask import jsonify, request
from flask.views import MethodView

from src.domain.errors import MissingParamError

from src.data.errors import UploadError
from src.main.factories.infra.mongo_client_factory import mongo_client_factory
from src.data.usecases import AddPhoto
from src.infra.s3.s3_photo_uploader import S3PhotoUploader
from src.infra.mongo.mongo_photo_repository import MongoPhotoRepository

photo_uploader = S3PhotoUploader()
photo_repository = MongoPhotoRepository(*mongo_client_factory(), "photos")
add_photo = AddPhoto(photo_uploader, photo_repository)


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
