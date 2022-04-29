from src.data.protocols import AbstractPasswordEncryptor


class PasswordEncryptorSpy(AbstractPasswordEncryptor):
    def __init__(self) -> None:
        self.hash = None
        self.encrypted_password = ""
        self.password = ""

    def encrypt_password(self, password) -> str:
        self.password = password
        self.encrypted_password = f"{self.hash}-{self.password}"
        return self.encrypted_password

    def check_password(self, password, hash: str) -> bool:
        return self.password == password
