from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from src.presentation.helpers.serializers import serialize_photo
from src.main.factories.infra import mongo_photo_repository_factory
from src.main.factories.infra import mongo_user_repository_factory


photo_repository = mongo_photo_repository_factory()
user_repository = mongo_user_repository_factory()


class ListPhotosController(MethodView):
    @jwt_required()
    def get(self):

        page = int(request.args.get("page"))
        user_id = request.args.get("user_id")

        if user_repository.find_user_by_id(user_id)["is_admin"]:
            filter_approved_photos = {}
        else:
            filter_approved_photos = {"approved": True}

        page = 1 if page <= 0 else page

        per_page = 10
        skips = per_page * (page - 1)

        photos = photo_repository.list_photos(skips, per_page, filter_approved_photos)
        return jsonify([serialize_photo(photo) for photo in photos]), 200
