from src.main.factories.infra.mongo_user_repository_factory import (
    mongo_user_repository_factory,
)
from src.main.factories.infra.passlib_password_encryptor_factory import (
    passlib_password_encryptor_factory,
)
from src.domain.usecases import AbstractAuthentication
from src.data.usecases import Authentication


def authentication_factory() -> AbstractAuthentication:
    return Authentication(
        mongo_user_repository_factory(), passlib_password_encryptor_factory()
    )
