import uuid
from app.users.services.auth_service import AuthService


class MockUserRepo:
    def create(self, user):
        return user


class MockRoleRepo:

    def get_by_name(self, name):
        class Role:
            id: uuid.uuid4()

        return Role


def test_register_user():
    service = AuthService(MockUserRepo(), MockRoleRepo())

    user = service.register("test@gmail.com", "admin")

    assert user.email == "test@gmail.com"
