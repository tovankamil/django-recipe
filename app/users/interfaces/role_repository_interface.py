import uuid
from typing import Optional
from abc import ABC, abstractmethod
from ..entities.role_entity import RoleEntity


class IRoleRepository(ABC):

    @abstractmethod
    def create(self, role: RoleEntity) -> RoleEntity:
        pass

    @abstractmethod
    def update(self, role: RoleEntity) -> RoleEntity:
        pass

    @abstractmethod
    def delete(self, role_id: uuid.UUID) -> None:
        pass

    @abstractmethod
    def get_by_id(self, role_id: uuid.UUID) -> Optional[RoleEntity]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[RoleEntity]:
        pass
