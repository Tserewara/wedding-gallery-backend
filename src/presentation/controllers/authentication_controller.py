from datetime import timedelta
from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import (
    create_access_token,
)
from src.domain.errors import WrongCredentialsError
from src.data.usecases import Authentication
from src.main.factories.infra import (
    mongo_user_repository_factory,
    passlib_password_encryptor_factory,
)

authentication = Authentication(
    mongo_user_repository_factory(), passlib_password_encryptor_factory()
)


class AuthenticationController(MethodView):
    def post(self):
        try:
            _, user_id = authentication.auth(
                email=request.json.get("email"), password=request.json.get("password")
            )

            access_token = create_access_token(
                identity=str(user_id), expires_delta=timedelta(minutes=30)
            )

            return jsonify({"token": access_token, "user_id": user_id}), 200

        except WrongCredentialsError as e:
            return jsonify(msg=str(e)), 403
