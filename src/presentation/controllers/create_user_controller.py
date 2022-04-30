from flask import jsonify, request
from flask.views import MethodView

from src.main.factories.domain.usecases.create_user_factory import create_user_factory
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

        except (EmailInUseError, MissingParamError) as e:
            status_code = 409 if type(e) == "MissingParamError" else 400
            return jsonify(msg=str(e)), status_code
