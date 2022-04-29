from src.data.protocols import AbstractUserRepository
from src.domain.models.user_model import UserModel
from src.domain.usecases import AbstractCreateUser


class CreateUser(AbstractCreateUser):
    def __init__(self, user_repository: AbstractUserRepository) -> None:
        super().__init__(user_repository)

    def create(self, name, email, password, is_admin):

        user = UserModel(name, email, is_admin, password)
        self.user_repository.add(user)
