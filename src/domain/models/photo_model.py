from dataclasses import dataclass


@dataclass
class PhotoModel:
    user_id: str
    username: str
    image_address: str
    is_approved: bool = False
