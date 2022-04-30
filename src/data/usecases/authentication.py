from src.data.protocols import AbstractPasswordEncryptor, AbstractUserRepository
from src.domain.usecases import AbstractAuthentication
from src.domain.models import UserModel
from src.domain.errors import WrongCredentialsError


class Authentication(AbstractAuthentication):
    def __init__(
        self,
        user_repository: AbstractUserRepository,
        password_encryptor: AbstractPasswordEncryptor,
    ) -> None:
        super().__init__(user_repository, password_encryptor)

    def auth(self, email, password):

        user: UserModel = self.user_repository.find_user_by_email(email)

        error = WrongCredentialsError("Wrong credentials. Verify email and password.")

        if not user:
            raise error

        result = self.password_encryptor.check_password(password, user["password"])

        if not result:
            raise error

        return result
