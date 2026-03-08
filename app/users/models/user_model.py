import uuid
from django.db import models
from .role_model import Role
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    class Meta:
        db_table = "users"
