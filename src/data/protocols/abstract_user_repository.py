import abc

from src.domain.models import UserModel


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: UserModel):
        raise NotImplementedError

    @abc.abstractmethod
    def find_user_by_email(self, email):
        raise NotImplementedError
