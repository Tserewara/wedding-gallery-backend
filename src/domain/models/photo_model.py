from dataclasses import dataclass


@dataclass
class PhotoModel:
    user_id: str
    image_address: str
    is_approved: bool = False
