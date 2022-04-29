import os
import uuid

import boto3
from botocore.exceptions import ClientError

from src.data.protocols import AbstractPhotoUploader


class S3PhotoUploader(AbstractPhotoUploader):
    def __init__(self) -> None:
        self._result = {"error": None, "message": ""}
        self._client = boto3.client(
            "s3",
            aws_access_key_id=os.environ.get("AWS_S3_ACCESS_KEY"),
            aws_secret_access_key=os.environ.get("SECRET_ACCESS_KEY"),
        )
        self._bucket = "picloader"

    def upload(self, file, filename) -> dict:
        try:
            hashed_filename = self._hash_filename(filename)
            self._client.upload_fileobj(file, self._bucket, hashed_filename)
            self._result["message"] = hashed_filename
            return self._result

        except ClientError as e:
            self._result["error"] = e
            return self._result

    def _hash_filename(self, filename):
        return f"{uuid.uuid4()}-{filename}"
