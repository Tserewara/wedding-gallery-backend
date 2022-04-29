import abc


class AbstractCreateUser(abc.ABC):
    def __init__(self, user_repository) -> None:
        self.user_repository = user_repository

    @abc.abstractmethod
    def create(self, name: str, email: str, password: str, is_admin: bool):
        raise NotImplementedError
