import uuid
from datetime import datetime

from .entities import (
    BaseEntity,
    UserEntity,
    RoleEntity,
    UserRoleEntity,
    PermissionEntity,
    RolePermissionEntity,
)


def test_base_entity_creation():
    entity = BaseEntity()

    assert isinstance(entity.id, uuid.UUID)
    assert isinstance(entity.created_at, datetime)
    assert isinstance(entity.updated_at, datetime)


def test_base_entity_with_custom_id():
    custom_id = uuid.uuid4()
    entity = BaseEntity(id=custom_id)

    assert entity.id == custom_id
    assert isinstance(entity.created_at, datetime)
    assert isinstance(entity.updated_at, datetime)


def test_user_entity_creation():
    user = UserEntity(
        email="test@example.com",
        password="hashed_password",
        first_name="John",
        last_name="Doe",
        phone_number="08123456789",
        roles=["admin"],
    )

    assert user.email == "test@example.com"
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.phone_number == "08123456789"
    assert user.roles == ["admin"]
    assert user.is_active is True
    assert isinstance(user.id, uuid.UUID)


def test_user_entity_default_values():
    user = UserEntity(
        email="test@example.com",
        first_name="Jane",
        last_name="Doe",
        password="password123",
    )

    assert user.email == "test@example.com"
    assert user.first_name == "Jane"
    assert user.last_name == "Doe"
    assert user.phone_number == ""
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False
    assert user.roles == []


def test_user_entity_default_roles():
    user = UserEntity(
        email="test@example.com", password="123", first_name="Jane", last_name="Doe"
    )

    assert user.roles == []


def test_role_entity_creation():
    role = RoleEntity(name="admin", description="Administrator role", is_active=True)

    assert role.name == "admin"
    assert role.description == "Administrator role"
    assert role.is_active is True


def test_role_entity_with_custom_id():
    custom_id = uuid.uuid4()
    role = RoleEntity(
        name="moderator", description="Moderator role", is_active=False, id=custom_id
    )

    assert role.name == "moderator"
    assert role.description == "Moderator role"
    assert role.is_active is False
    assert role.id == custom_id


def test_user_role_entity_creation():
    user_id = uuid.uuid4()
    role_id = uuid.uuid4()
    assigned_by = uuid.uuid4()

    user_role = UserRoleEntity(
        user_id=user_id, role_id=role_id, assigned_by=assigned_by
    )

    assert user_role.user_id == user_id
    assert user_role.role_id == role_id
    assert user_role.assigned_by == assigned_by
    assert isinstance(user_role.assigned_at, datetime)
    assert isinstance(user_role.id, uuid.UUID)


def test_can_add_permission_entity_creation():
    permission = PermissionEntity(
        name="Can add user", codename="add_user", description="Allows adding users"
    )

    assert permission.name == "Can add user"
    assert permission.codename == "add_user"
    assert permission.description == "Allows adding users"


def test_role_permission_entity_creation():
    role_id = uuid.uuid4()
    permission_id = uuid.uuid4()
    granted_by = uuid.uuid4()

    role_permission = RolePermissionEntity(
        role_id=role_id, permission_id=permission_id, granted_by=granted_by
    )

    assert role_permission.role_id == role_id
    assert role_permission.permission_id == permission_id
    assert role_permission.granted_by == granted_by
    assert isinstance(role_permission.granted_at, datetime)
    assert isinstance(role_permission.id, uuid.UUID)


def test_create_permission_entity_creation():
    permission = PermissionEntity(
        name="Create User", codename="create_user", description="Allow creating user"
    )

    assert permission.name == "Create User"
    assert permission.codename == "create_user"
    assert permission.description == "Allow creating user"
