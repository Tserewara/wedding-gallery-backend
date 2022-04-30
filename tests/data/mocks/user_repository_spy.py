from typing import List
import uuid

from src.domain.models import UserModel
from src.data.protocols import AbstractUserRepository


class UserRepositorySpy(AbstractUserRepository):
    def __init__(self) -> None:
        self.users: List = []

    def add(self, user: UserModel) -> None:
        self.users.append(
            {
                "_id": uuid.uuid4(),
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "is_admin": user.is_admin,
            }
        )

    def find_user_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user

    def find_user_by_id(self, user_id: str):
        if not self.users:
            return None
        return self.users[int(user_id)]
