from abc import ABC, abstractmethod
from ..entities.user_entity import UserEntity


class IAuthService(ABC):

    @abstractmethod
    def register(self, email: str, role_name=id) -> UserEntity:
        pass
