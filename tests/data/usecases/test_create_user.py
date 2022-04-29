from src.domain.models import UserModel
from src.data.usecases import CreateUser
from src.data.protocols import AbstractUserRepository


class UserRepositorySpy(AbstractUserRepository):
    def __init__(self) -> None:
        self.users = []

    def add(self, user: UserModel) -> None:
        self.users.append(user)


def test_should_add_user_created_to_repository():
    name = "a_username"
    email = "random@example.com"
    password = "Secure_Password"
    is_admin = True
    user_repository_spy = UserRepositorySpy()
    sut = CreateUser(user_repository_spy)
    sut.create(name, email, password, is_admin)

    assert len(user_repository_spy.users) == 1
