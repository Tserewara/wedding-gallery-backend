import pytest

from src.domain.errors import EmailInUseError
from src.data.usecases import CreateUser

from tests.data.mocks.user_repository_spy import UserRepositorySpy
from tests.data.mocks.password_encryptor_spy import PasswordEncryptorSpy
from tests.domain.models.mocks.mock_user_params import mock_user_params


def make_sut():
    user_repository_spy = UserRepositorySpy()
    password_encryptor_spy = PasswordEncryptorSpy()
    sut = CreateUser(user_repository_spy, password_encryptor_spy)
    return sut, user_repository_spy, password_encryptor_spy


def test_should_add_user_created_to_repository():
    name, email, password, is_admin = mock_user_params()

    sut, user_repository_spy, _ = make_sut()
    sut.create(name, email, password, is_admin)

    assert len(user_repository_spy.users) == 1


def test_should_raise_email_in_user_error_if_email_already_exists():
    name, email, password, is_admin = mock_user_params()

    sut, _, _ = make_sut()
    sut.create(name, email, password, is_admin)

    with pytest.raises(EmailInUseError):
        sut.create(name, email, password, is_admin)


def test_should_encrypt_password_when_creating_user():
    name, email, password, is_admin = mock_user_params()

    fake_hash = "78asd"

    sut, _, password_encryptor_spy = make_sut()

    password_encryptor_spy.hash = fake_hash

    user = sut.create(name, email, password, is_admin)

    assert user.password == f"{fake_hash}-{password}"
