import uuid
import pytest

from app.users.repositories.role_repository import RoleRepository
from app.users.entities.role_entity import RoleEntity


@pytest.mark.django_db
def test_create_role():
    repo = RoleRepository()
    role = RoleEntity(id=uuid.uuid4(), name="admin", permission=[])

    result = repo.create(role)

    assert result.name == "admin"
