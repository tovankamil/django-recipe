import uuid
from dataclasses import dataclass
from .role_entity import RoleEntity


@dataclass
class UserEntity:
    id: uuid.UUID
    email: str
    first_name: str
    last_name: str
    role: RoleEntity
