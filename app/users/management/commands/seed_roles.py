from django.core.management.base import BaseCommand
from app.users.models.role_model import Role


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        roles = ["admin", "member", "finance"]

        for role in roles:
            Role.objects.get_or_create(name=role)

        self.stdout.write(self.style.SUCCESS("Roles seeded"))
