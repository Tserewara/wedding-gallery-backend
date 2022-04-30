from flask import jsonify, request
from flask.views import MethodView

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

            add_photo.add(
                user_id=request.form.get("user_id"), filename=file.filename, file=file
            )

            return jsonify(msg="photo added successfully"), 201

        except UploadError as e:
            return jsonify(msg=str(e))
