from src.data.protocols import AbstractPasswordEncryptor
from src.domain.errors import EmailInUseError
from src.data.protocols import AbstractUserRepository
from src.domain.models.user_model import UserModel
from src.domain.usecases import AbstractCreateUser


class CreateUser(AbstractCreateUser):
    def __init__(
        self,
        user_repository: AbstractUserRepository,
        password_encryptor: AbstractPasswordEncryptor,
    ) -> None:
        super().__init__(user_repository, password_encryptor)

    def create(
        self,
        name: str,
        email: str,
        password: str,
        is_admin: bool,
    ) -> UserModel:

        if self.user_repository.find_user_by_email(email):
            raise EmailInUseError("Email already in use")

        password_encrypted = self.password_encryptor.encrypt_password(password)
        user = UserModel(name, email, is_admin, password_encrypted)

        self.user_repository.add(user)

        return user
