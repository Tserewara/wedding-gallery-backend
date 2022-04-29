from faker import Faker
from src.data.protocols import AbstractPhotoUploader


class PhotoUploaderSpy(AbstractPhotoUploader):
    def __init__(self) -> None:
        super().__init__()
        self.file: str = ""
        self.filename: str = ""
        self.hash = ""

    def upload(self, file, filename):
        self.file = file
        self.filename = filename
        return f"{self.hash}-{self.filename}"
