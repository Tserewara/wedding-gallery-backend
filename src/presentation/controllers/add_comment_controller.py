from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from src.main.factories.domain.usecases import add_comment_factory


add_comment = add_comment_factory()


class AddCommentController(MethodView):
    @jwt_required()
    def post(self):

        add_comment.comment(
            user_id=request.json.get("user_id"),
            photo_id=request.json.get("photo_id"),
            text=request.json.get("text"),
        )

        return ("", 204)
