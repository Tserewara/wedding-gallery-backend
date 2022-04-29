import abc


class AbstractPasswordEncryptor(abc.ABC):
    @abc.abstractmethod
    def encrypt_password(self, password: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def check_password(self, password: str, hash: str) -> bool:
        raise NotImplementedError
