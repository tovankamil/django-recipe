import uuid
from ..interfaces.role_repository_interface import IRoleRepository
from ..entities.role_entity import RoleEntity


class RoleService:

    def __init__(self, role_repository: IRoleRepository):
        self.role_repo = role_repository

    def create(self, name: str):
        role = RoleEntity(id=uuid.uuid4(), name=name, permissionEntity=[])

        return self.role_repo.create(role)
