from typing import Tuple
import pytest

from src.data.usecases import Authentication

from src.domain.errors import WrongCredentialsError
from src.domain.models import UserModel

from tests.data.mocks.user_repository_spy import UserRepositorySpy
from tests.data.mocks.password_encryptor_spy import PasswordEncryptorSpy


def make_sut() -> Tuple[Authentication, UserRepositorySpy, PasswordEncryptorSpy]:
    user_repository_spy = UserRepositorySpy()
    password_encryptor_spy = PasswordEncryptorSpy()
    password_encryptor_spy.hash = "14a5s6"

    sut = Authentication(user_repository_spy, password_encryptor_spy)

    return sut, user_repository_spy, password_encryptor_spy


def mock_authentication_params(
    email: str = "user@example.com", password: str = "any_password"
) -> Tuple[str]:
    return email, password


def test_should_return_true_if_authentication_succeeds():
    sut, user_repository_spy, password_encryptor_spy = make_sut()

    email, password = mock_authentication_params()

    password_encrypted = password_encryptor_spy.encrypt_password(password)

    user_repository_spy.add(UserModel("any_username", email, password_encrypted))

    sut = Authentication(user_repository_spy, password_encryptor_spy)

    assert sut.auth(email, password)


def test_should_raise_wrong_credentials_error_if_email_is_not_found():
    sut, user_repository_spy, password_encryptor_spy = make_sut()

    email, password = mock_authentication_params()
    password = password_encryptor_spy.encrypt_password(password)

    sut = Authentication(user_repository_spy, password_encryptor_spy)

    with pytest.raises(WrongCredentialsError):
        sut.auth(email, password)


def test_should_raise_wrong_credentials_error_if_password_is_wrong():
    sut, user_repository_spy, password_encryptor_spy = make_sut()

    email = "user@example.com"
    password = password_encryptor_spy.encrypt_password("any_password")

    sut = Authentication(user_repository_spy, password_encryptor_spy)
    user_repository_spy.add(UserModel("any_username", email, password))

    with pytest.raises(WrongCredentialsError):
        sut.auth(email, "wrong_password")
