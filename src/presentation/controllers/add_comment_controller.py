from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from src.main.factories.infra import mongo_user_repository_factory
from src.main.factories.domain.usecases import add_comment_factory


add_comment = add_comment_factory()
user_repository = mongo_user_repository_factory()


class AddCommentController(MethodView):
    @jwt_required()
    def post(self):

        user_id = request.json.get("user_id")
        username = user_repository.find_user_by_id(user_id)["name"]

        add_comment.comment(
            username=username,
            photo_id=request.json.get("photo_id"),
            text=request.json.get("text"),
        )

        return ("", 204)
