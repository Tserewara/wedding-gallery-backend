from dataclasses import dataclass


@dataclass
class UserModel:
    name: str
    email: str
    is_admin: bool
    password: str
