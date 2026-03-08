import uuid
from app.users.entities.role_entity import RoleEntity


def test_role_entity():
    role = RoleEntity(id=uuid.uuid4(), name="admin", permissionEntity=[])

    assert role.name == "admin"
