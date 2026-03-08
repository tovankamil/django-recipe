import uuid
from django.db import models
from .role_model import Role


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    class Meta:
        db_table = "users"
