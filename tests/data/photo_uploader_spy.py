from src.data.protocols import AbstractPhotoUploader


class PhotoUploaderSpy(AbstractPhotoUploader):
    file: str
    filename: str

    def upload(self, file, filename):
        self.file = file
        self.filename = filename
