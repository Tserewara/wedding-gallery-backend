import pytest

from src.data.usecases import Authentication

from src.domain.errors import WrongCredentialsError
from src.domain.models import UserModel

from tests.data.mocks.user_repository_spy import UserRepositorySpy
from tests.data.mocks.password_encryptor_spy import PasswordEncryptorSpy


def test_should_return_true_if_authentication_succeeds():
    user_repository_spy = UserRepositorySpy()
    password_encryptor_spy = PasswordEncryptorSpy()
    password_encryptor_spy.hash = "14a5s6"

    email = "user@example.com"
    password = password_encryptor_spy.encrypt_password("any_password")

    user_repository_spy.add(UserModel("any_username", email, password))

    sut = Authentication(user_repository_spy, password_encryptor_spy)
    result = sut.auth(email, password)
    assert result == True


def test_should_raise_wrong_credentials_error_if_email_is_not_found():
    user_repository_spy = UserRepositorySpy()
    password_encryptor_spy = PasswordEncryptorSpy()
    password_encryptor_spy.hash = "14a5s6"

    email = "user@example.com"
    password = password_encryptor_spy.encrypt_password("any_password")

    sut = Authentication(user_repository_spy, password_encryptor_spy)

    with pytest.raises(WrongCredentialsError):
        sut.auth(email, password)


def test_should_raise_wrong_credentials_error_if_password_is_wrong():
    user_repository_spy = UserRepositorySpy()
    password_encryptor_spy = PasswordEncryptorSpy()
    password_encryptor_spy.hash = "14a5s6"

    email = "user@example.com"
    password = password_encryptor_spy.encrypt_password("any_password")

    sut = Authentication(user_repository_spy, password_encryptor_spy)
    user_repository_spy.add(UserModel("any_username", email, password))

    with pytest.raises(WrongCredentialsError):
        sut.auth(email, "wrong_password")
