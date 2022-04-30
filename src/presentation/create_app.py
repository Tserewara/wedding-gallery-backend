from flask import Flask
from src.presentation.controllers.users_controller import UsersController


def create_app() -> Flask:
    app = Flask(__name__)

    app.add_url_rule(
        "/users", methods=["POST"], view_func=UsersController.as_view("users")
    )

    return app


create_app().run(debug=True)
