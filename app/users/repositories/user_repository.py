from ..interfaces.user_repository_interface import IUserRepository
from ..models.user_model import User
from ..entities.user_entity import UserEntity


class UserRepository(IUserRepository):
    def create(self, user: UserEntity) -> UserEntity:
        User.objects.create(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            role_id=user.role.id,
        )

        return user
