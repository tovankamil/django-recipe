import uuid
from typing import Optional, Dict, Any

from ..interfaces.role_repository_interface import IRoleRepository
from ..entities.role_entity import RoleEntity


class RoleService:

    def __init__(self, role_repository: IRoleRepository):
        self.role_repo = role_repository

    def create(self, name: str) -> RoleEntity:

        existing = self.role_repo.get_by_name(name)

        if existing:
            raise ValueError("Role already exists")

        role = RoleEntity(id=uuid.uuid4(), name=name, permissions=[])

        return self.role_repo.create(role)

    def update(self, role_id: uuid.UUID, name: str) -> RoleEntity:

        role = self.role_repo.get_by_id(role_id)

        if not role:
            raise ValueError("Role not found")

        role.name = name

        return self.role_repo.update(role)

    def delete(self, role_id: uuid.UUID) -> None:

        role = self.role_repo.get_by_id(role_id)

        if not role:
            raise ValueError("Role not found")

        self.role_repo.delete(role_id)

    def get_by_id(self, role_id: uuid.UUID) -> RoleEntity:

        role = self.role_repo.get_by_id(role_id)

        if not role:
            raise ValueError("Role not found")

        return role

    def get_by_name(self, name: str) -> RoleEntity:

        role = self.role_repo.get_by_name(name)

        if not role:
            raise ValueError("Role not found")

        return role

    def list(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:

        roles, total = self.role_repo.list(page, page_size)

        return {
            "data": roles,
            "meta": {"page": page, "page_size": page_size, "total": total},
        }
