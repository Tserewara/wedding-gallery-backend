from flask import jsonify, request
from flask.views import MethodView

from src.main.factories.domain.usecases import create_user_factory
from src.domain.errors import EmailInUseError, MissingParamError


create_user = create_user_factory()


class CreateUserController(MethodView):
    def post(self):

        try:

            create_user.create(
                name=request.json.get("name"),
                email=request.json.get("email"),
                password=request.json.get("password"),
                is_admin=request.json.get("is_admin"),
            )

            return jsonify(msg="user created successfully"), 201

        except EmailInUseError as e:
            return jsonify(msg=str(e)), 409
        except MissingParamError as e:
            return jsonify(msg=str(e)), 400
