from typing import List

from src.domain.models import UserModel
from src.data.protocols import AbstractUserRepository


class UserRepositorySpy(AbstractUserRepository):
    def __init__(self) -> None:
        self.users: List[UserModel] = []

    def add(self, user: UserModel) -> None:
        self.users.append(user)

    def find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user

    def find_user_by_id(self, user_id: str):
        if not self.users:
            return None
        return self.users[int(user_id)]
