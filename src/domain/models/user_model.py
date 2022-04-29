from dataclasses import dataclass


@dataclass
class UserModel:
    name: str
    email: str
    password: str
    is_admin: bool = False
