from src.infra.s3.s3_photo_uploader import S3PhotoUploader


def s3_photo_uploader_factory():
    return S3PhotoUploader()
