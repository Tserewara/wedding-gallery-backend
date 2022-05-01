from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from src.presentation.helpers.serializers import serialize_photo
from src.main.factories.infra.mongo_photo_repository_factory import (
    mongo_photo_repository_factory,
)

photo_repository = mongo_photo_repository_factory()


class ListPhotosController(MethodView):
    @jwt_required()
    def get(self):

        page = int(request.args.get("page"))

        page = 1 if page <= 0 else page

        per_page = 10
        skips = per_page * (page - 1)

        photos = photo_repository.list_approved_photos(skips, per_page)
        return jsonify([serialize_photo(photo) for photo in photos]), 200
