import uuid
from typing import Optional, List, Tuple

from ..interfaces.role_repository_interface import IRoleRepository
from ..entities.role_entity import RoleEntity
from ..models.role_model import Role


class RoleRepository(IRoleRepository):

    def create(self, role: RoleEntity) -> RoleEntity:

        role_model = Role.objects.create(id=role.id, name=role.name)

        return RoleEntity(id=role_model.id, name=role_model.name, permissions=[])

    def update(self, role: RoleEntity) -> RoleEntity:

        role_model = Role.objects.get(id=role.id)

        role_model.name = role.name
        role_model.save(update_fields=["name"])

        return RoleEntity(id=role_model.id, name=role_model.name, permissions=[])

    def delete(self, role_id: uuid.UUID) -> None:

        Role.objects.filter(id=role_id).delete()

    def get_by_id(self, role_id: uuid.UUID) -> Optional[RoleEntity]:

        role = Role.objects.filter(id=role_id).first()

        if not role:
            return None

        return RoleEntity(id=role.id, name=role.name, permissions=[])

    def get_by_name(self, name: str) -> Optional[RoleEntity]:

        role = Role.objects.filter(name=name).first()

        if not role:
            return None

        return RoleEntity(id=role.id, name=role.name, permissions=[])

    def list(self, page: int, page_size: int) -> Tuple[List[RoleEntity], int]:

        offset = (page - 1) * page_size

        queryset = Role.objects.all().order_by("name")

        total = queryset.count()

        roles = queryset[offset : offset + page_size]

        role_entities = [
            RoleEntity(id=r.id, name=r.name, permissions=[]) for r in roles
        ]

        return role_entities, total
