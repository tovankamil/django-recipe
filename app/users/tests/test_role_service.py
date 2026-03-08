import pytest
from app.users.repositories.role_repository import RoleRepository
from app.users.services.role_service import RoleService


@pytest.fixture
def service():
    repo = RoleRepository()
    return RoleService(repo)


@pytest.mark.django_db
def test_role_list(service):

    result = service.list(page=1, page_size=10)

    assert "data" in result
    assert "total" in result
