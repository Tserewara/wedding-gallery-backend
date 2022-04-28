import abc


class AbstractPhotoUploader(abc.ABC):
    @abc.abstractmethod
    def upload(self, file, filename):
        raise NotImplementedError
