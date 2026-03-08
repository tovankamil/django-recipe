from typing import Optional
from ..models import user_model
import uuid
from ..entities import role_entity
from ..interfaces.user_interface import IUserRepository


class UserRepository(IUserRepository):

    def create(self, user_entity: role_entity.UserEntity) -> role_entity.UserEntity:
        """Create a new user entity in the database"""

        user = user_model.User.objects.create(
            id=user_entity.id,
            email=user_entity.email,
            first_name=user_entity.first_name,
            last_name=user_entity.last_name,
            phone_number=user_entity.phone_number,
            is_active=user_entity.is_active,
            is_staff=user_entity.is_staff,
            is_superuser=user_entity.is_superuser,
        )
        # Set password separately to ensure proper hashing
        user.set_password(user_entity.password)
        user.save()

        # Update the entity with the saved model data
        user_entity.id = user.id
        return user_entity

    def get_by_id(self, user_id: uuid.UUID) -> Optional[role_entity.UserEntity]:
        """Get user by ID from the database"""

        try:
            user = user_model.User.objects.get(id=user_id)
            return role_entity.UserEntity(
                id=user.id,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                phone_number=user.phone_number,
                is_active=user.is_active,
                is_staff=user.is_staff,
                is_superuser=user.is_superuser,
                password=user.password,
            )
        except user_model.User.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> Optional[role_entity.UserEntity]:
        """Get user by email from the database"""

        try:
            user = user_model.User.objects.get(email=email)
            return role_entity.UserEntity(
                id=user.id,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                phone_number=user.phone_number,
                is_active=user.is_active,
                is_staff=user.is_staff,
                is_superuser=user.is_superuser,
                password=user.password,
            )
        except user_model.User.DoesNotExist:
            return None

    def authenticate_user(
        self, email: str, password: str
    ) -> Optional[role_entity.UserEntity]:
        """Authenticate user by email and password"""

        try:
            user = user_model.User.objects.get(email=email)
            # Django's built-in password checking
            if user.check_password(password):
                return role_entity.UserEntity(
                    id=user.id,
                    email=user.email,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    phone_number=user.phone_number,
                    is_active=user.is_active,
                    is_staff=user.is_staff,
                    is_superuser=user.is_superuser,
                    password=user.password,
                )
            return None
        except user_model.User.DoesNotExist:
            return None
