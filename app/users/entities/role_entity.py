import uuid
from dataclasses import dataclass
from typing import List


@dataclass
class PermissionEntity:
    id: uuid.UUID
    name: str


@dataclass
class RoleEntity:
    id: uuid.UUID
    name: str
    permission: List[PermissionEntity]
