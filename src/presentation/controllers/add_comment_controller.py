from flask import request
from flask.views import MethodView

from src.main.factories.infra.mongo_photo_repository_factory import (
    mongo_photo_repository_factory,
)

from src.data.usecases import AddComment

add_comment = AddComment(mongo_photo_repository_factory())


class AddCommentController(MethodView):
    def post(self):

        add_comment.comment(
            user_id=request.json.get("user_id"),
            photo_id=request.json.get("photo_id"),
            text=request.json.get("text"),
        )

        return ("", 204)
