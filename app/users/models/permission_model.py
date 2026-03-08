import uuid
from django.db import models


class Permission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "permissions"
