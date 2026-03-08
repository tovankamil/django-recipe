from abc import ABC, abstractmethod
from ..entities.user_entity import UserEntity


class IUserRepository(ABC):

    @abstractmethod
    def create(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity:
        pass
