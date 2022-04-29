import pytest

from src.domain.errors import EmailInUseError
from src.data.usecases import CreateUser

from tests.data.mocks.user_repository_spy import UserRepositorySpy
from tests.data.mocks.password_encryptor_spy import PasswordEncryptorSpy


def test_should_add_user_created_to_repository():
    name = "a_username"
    email = "random@example.com"
    password = "Secure_Password"
    is_admin = True
    user_repository_spy = UserRepositorySpy()
    password_encryptor = PasswordEncryptorSpy()
    sut = CreateUser(user_repository_spy, password_encryptor)
    sut.create(name, email, password, is_admin)

    assert len(user_repository_spy.users) == 1


def test_should_raise_email_in_user_error_if_email_already_exists():
    name = "a_username"
    email = "random@example.com"
    password = "Secure_Password"
    is_admin = True
    user_repository_spy = UserRepositorySpy()
    password_encryptor = PasswordEncryptorSpy()
    sut = CreateUser(user_repository_spy, password_encryptor)
    sut.create(name, email, password, is_admin)

    with pytest.raises(EmailInUseError):
        sut.create(name, email, password, is_admin)


def test_encrypt_password_when_creating_user():
    name = "a_username"
    email = "random@example.com"
    password = "Secure@Password"
    is_admin = True
    user_repository_spy = UserRepositorySpy()
    password_encryptor = PasswordEncryptorSpy()
    fake_hash = "78asd"
    password_encryptor.hash = fake_hash

    sut = CreateUser(user_repository_spy, password_encryptor)

    user = sut.create(name, email, password, is_admin)

    assert user.password == f"{fake_hash}-{password}"
