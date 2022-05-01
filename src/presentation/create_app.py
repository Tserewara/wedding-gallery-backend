import os
from flask import Flask
from flask_jwt_extended import JWTManager

from src.presentation.controllers import (
    AddCommentController,
    AddPhotoController,
    ApprovePhotoController,
    AuthenticationController,
    CreateUserController,
    LikePhotoController,
    ListPhotosController,
)


def create_app() -> Flask:

    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
    JWTManager(app)

    app.add_url_rule(
        "/register",
        methods=["POST"],
        view_func=CreateUserController.as_view("register"),
    )

    app.add_url_rule(
        "/login", methods=["POST"], view_func=AuthenticationController.as_view("login")
    )

    app.add_url_rule(
        "/photos",
        methods=["POST"],
        view_func=AddPhotoController.as_view("photos"),
    )

    app.add_url_rule(
        "/photos",
        methods=["GET"],
        view_func=ListPhotosController.as_view("list_photos"),
    )

    app.add_url_rule(
        "/photos",
        methods=["PATCH"],
        view_func=ApprovePhotoController.as_view("approve_photo"),
    )

    app.add_url_rule(
        "/like",
        methods=["POST"],
        view_func=LikePhotoController.as_view("like_photo"),
    )

    app.add_url_rule(
        "/comment",
        methods=["POST"],
        view_func=AddCommentController.as_view("comment_photo"),
    )

    return app


create_app().run(debug=True)
