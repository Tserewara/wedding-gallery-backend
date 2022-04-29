import abc

from src.data.protocols import AbstractUserRepository
from src.data.protocols import AbstractPasswordEncryptor


class AbstractAuthentication(abc.ABC):
    def __init__(
        self,
        user_repository: AbstractUserRepository,
        password_encryptor: AbstractPasswordEncryptor,
    ) -> None:
        self.user_repository = user_repository
        self.password_encryptor = password_encryptor

    @abc.abstractmethod
    def auth(self, email, password):
        raise NotImplementedError
