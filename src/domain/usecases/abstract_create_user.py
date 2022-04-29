import abc


class AbstractCreateUser(abc.ABC):
    def __init__(self, user_repository, password_encryptor) -> None:
        self.user_repository = user_repository
        self.password_encryptor = password_encryptor

    @abc.abstractmethod
    def create(self, name: str, email: str, password: str, is_admin: bool):
        raise NotImplementedError
