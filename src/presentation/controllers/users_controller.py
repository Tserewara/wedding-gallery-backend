from flask import jsonify, request
from flask.views import MethodView
from pymongo import MongoClient

from src.domain.errors import EmailInUseError
from src.data.usecases import CreateUser
from src.infra.mongo_user_repository import MongoUserRepository
from src.infra.passlib_password_encryptor import PasslibPasswordEncryptor


from src.infra.mongo_client import client

user_repository = MongoUserRepository(client, "friends-gallery", "users")
password_encryptor = PasslibPasswordEncryptor()

create_user = CreateUser(user_repository, password_encryptor)


class UsersController(MethodView):
    def post(self):

        create_user.create(
            name=request.json.get("name"),
            email=request.json.get("email"),
            password=request.json.get("password"),
            is_admin=request.json.get("is_admin"),
        )

        return jsonify(msg="user created successfully"), 201
