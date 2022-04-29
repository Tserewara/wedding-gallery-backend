from src.data.protocols import AbstractPhotoRepository, AbstractUserRepository
from src.domain.usecases import AbstractApprovePhoto
from src.domain.models import UserModel, PhotoModel
from src.domain.errors import (
    PermissionDeniedError,
    UserNotFoundError,
    PhotoNotFoundError,
)


class ApprovePhoto(AbstractApprovePhoto):
    def __init__(
        self,
        photo_repository: AbstractPhotoRepository,
        user_repository: AbstractUserRepository,
    ) -> None:
        super().__init__(photo_repository, user_repository)

    def approve(self, user_id, photo_id):

        user: UserModel = self.user_repository.find_user_by_id(user_id)
        if not user:
            raise UserNotFoundError("User not found")

        photo: PhotoModel = self.photo_repository.find_photo_by_id(photo_id)
        if not photo:
            raise PhotoNotFoundError("Photo not found")

        if not user.is_admin:
            raise PermissionDeniedError("You don't have permission to approve photos")

        self.photo_repository.update_photo(photo_id, "is_admin", True)
