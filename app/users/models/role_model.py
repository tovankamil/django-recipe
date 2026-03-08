import uuid
from django.db import models


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "roles"
