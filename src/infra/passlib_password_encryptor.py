from passlib.hash import pbkdf2_sha256

from src.data.protocols import AbstractPasswordEncryptor


class PasslibPasswordEncryptor(AbstractPasswordEncryptor):
    def encrypt_password(self, password: str) -> str:
        return pbkdf2_sha256.hash(password)

    def check_password(self, password: str, hash: str) -> bool:
        return pbkdf2_sha256.verify(password, hash)
