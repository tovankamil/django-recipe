import uuid
from ..interfaces.auth_service_interface import IAuthService
from ..interfaces.user_repository_interface import IUserRepository
from ..interfaces.role_repository_interface import IRoleRepository

from ..entities.user_entity import UserEntity


class AuthService(IAuthService):
    def __init__(
        self, user_repository=IUserRepository, role_repository=IRoleRepository
    ):
        self.user_repository = user_repository
        self.role_repository = role_repository

    def register(self, email: str, role_name: str):
        role = self.role_repository.get_by_name(role_name)
        user = UserEntity(
            id=uuid.uuid4(), email=email, first_name="", last_name="", role=role
        )

        return self.user_repository.create(user)
