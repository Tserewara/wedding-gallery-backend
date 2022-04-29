from src.data.protocols import AbstractUserRepository, AbstractPasswordEncryptor
from src.domain.models.user_model import UserModel
from src.domain.usecases.abstract_authentication import AbstractAuthentication

from tests.data.mocks.user_repository_spy import UserRepositorySpy
from tests.data.mocks.password_encryptor_spy import PasswordEncryptorSpy


class Authentication(AbstractAuthentication):
    def __init__(
        self,
        user_repository: AbstractUserRepository,
        password_encryptor: AbstractPasswordEncryptor,
    ) -> None:
        super().__init__(user_repository, password_encryptor)

    def auth(self, email, password):
        user: UserModel = self.user_repository.find_user_by_email(email)
        print(user.password)
        return self.password_encryptor.check_password(password, user.password)


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
