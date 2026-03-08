from django.db import models
from .role_model import Role
from .permission_model import Permission


class RolePermission(models.Model):
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="role_permission"
    )
    permission = models.ForeignKey(
        Permission, on_delete=models.CASCADE, related_name="permission_role"
    )

    class Meta:
        db_table = "role_permissions"
        constraints = [
            models.UniqueConstraint(
                fields=["role", "permission"], name="unique_role_permission"
            )
        ]
