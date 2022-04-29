from src.data.protocols import AbstractPasswordEncryptor


class PasswordEncryptorSpy(AbstractPasswordEncryptor):
    def __init__(self) -> None:
        self.hash = None
        self.encrypted_password = ""

    def encrypt_password(self, password) -> str:
        self.encrypted_password = f"{self.hash}-{password}"
        return self.encrypted_password

    def check_password(self, password) -> bool:
        return password == self.encrypted_password.strip(f"{self.hash}-")
