from src.data.protocols import AbstractPhotoUploader


class PhotoUploaderSpy(AbstractPhotoUploader):
    def __init__(self) -> None:
        super().__init__()
        self.file: str = ""
        self.filename: str = ""
        self.result = {"error": None, "message": "success"}

    def upload(self, file, filename):

        if self.result["error"]:
            raise self.result["error"]

        self.file = file
        self.filename = filename
        self.result["message"] = f"{self.filename}"

        return self.result
