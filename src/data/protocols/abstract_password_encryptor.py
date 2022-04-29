import abc


class AbstractPasswordEncryptor(abc.ABC):
    @abc.abstractmethod
    def encrypt_password(self, password) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def check_password(self, password) -> bool:
        raise NotImplementedError
