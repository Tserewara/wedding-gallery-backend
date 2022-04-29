import abc


class AbstractCreateUser(abc.ABC):
    @abc.abstractmethod
    def create_user(self, name, email, password):
        raise NotImplementedError
