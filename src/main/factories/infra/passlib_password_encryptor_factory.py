from src.infra.passlib import PasslibPasswordEncryptor


def passlib_password_encryptor_factory():
    return PasslibPasswordEncryptor()
