import uuid
from typing import Optional

from ..interfaces.role_repository_interface import IRoleRepository
from ..entities.role_entity import RoleEntity
from ..models.role_model import Role


class RoleRepository(IRoleRepository):

    def create(self, role: RoleEntity) -> RoleEntity:

        role_model = Role.objects.create(id=role.id, name=role.name)

        return RoleEntity(id=role_model.id, name=role_model.name, permissionEntity=[])

    def update(self, role: RoleEntity) -> RoleEntity:

        role_model = Role.objects.get(id=role.id)
        role_model.name = role.name
        role_model.save()

        return RoleEntity(id=role_model.id, name=role_model.name, permissionEntity=[])

    def delete(self, role_id: uuid.UUID) -> None:

        Role.objects.filter(id=role_id).delete()

    def get_by_id(self, role_id: uuid.UUID) -> Optional[RoleEntity]:

        try:
            role = Role.objects.get(id=role_id)
        except Role.DoesNotExist:
            return None

        return RoleEntity(id=role.id, name=role.name, permissionEntity=[])

    def get_by_name(self, name: str) -> Optional[RoleEntity]:

        try:
            role = Role.objects.get(name=name)
        except Role.DoesNotExist:
            return None

        return RoleEntity(id=role.id, name=role.name, permissionEntity=[])
