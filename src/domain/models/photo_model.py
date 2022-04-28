from dataclasses import dataclass, field
from typing import List


@dataclass
class PhotoModel:
    user_id: str
    image_address: str
    likes: int = 0
    comments: List = field(default_factory=lambda: [])
