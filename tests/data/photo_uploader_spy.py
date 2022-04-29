from faker import Faker
from src.data.protocols import AbstractPhotoUploader


class PhotoUploaderSpy(AbstractPhotoUploader):
    def __init__(self) -> None:
        super().__init__()
        self.file: str = ""
        self.filename: str = ""
        self.hash = ""
        self.error = None

    def upload(self, file, filename):
        if self.error:
            raise self.error()
        self.file = file
        self.filename = filename
        return f"{self.hash}-{self.filename}"
