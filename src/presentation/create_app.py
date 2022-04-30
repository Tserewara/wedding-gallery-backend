import os
from flask import Flask
from flask_jwt_extended import JWTManager

from src.presentation.controllers.authentication_controller import (
    AuthenticationController,
)
from src.presentation.controllers.create_user_controller import CreateUserController


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
    JWTManager(app)

    app.add_url_rule(
        "/users", methods=["POST"], view_func=CreateUserController.as_view("users")
    )

    app.add_url_rule(
        "/login", methods=["POST"], view_func=AuthenticationController.as_view("login")
    )

    return app


create_app().run(debug=True)
