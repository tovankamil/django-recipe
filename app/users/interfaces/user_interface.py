from abc import ABC, abstractmethod
from typing import Optional
import uuid
from ..entities import role_entity

# Type alias to reduce line length
UserOpt = Optional[role_entity.UserEntity]


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user_entity: UserOpt) -> UserOpt:
        """Create a new user entity"""
        pass

    @abstractmethod
    def get_by_id(self, user_id: uuid.UUID) -> Optional[UserOpt]:
        """Get user by ID"""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserOpt]:
        """Get user by email"""
        pass

    @abstractmethod
    def authenticate_user(self, email: str, password: str) -> Optional[UserOpt]:
        """Authenticate user by email and password"""
        pass
