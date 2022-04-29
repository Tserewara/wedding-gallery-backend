import abc


class AbstractLikePhoto(abc.ABC):
    def __init__(self, photo_repository) -> None:
        self.photo_repository = photo_repository

    @abc.abstractmethod
    def like(self, user_id, photo_id):
        raise NotImplementedError
