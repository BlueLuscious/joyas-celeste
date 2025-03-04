from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from app.settings import FIRST_ADMIN_PASSWORD, FIRST_ADMIN_USERNAME


class Command(BaseCommand):

    """ Command to create the first superuser. """

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.count() == 0:
            username = FIRST_ADMIN_USERNAME
            email = "admin@admin.com"
            password = FIRST_ADMIN_PASSWORD

            admin = User.objects.create_superuser(
                email=email, username=username, password=password
            )
            admin.is_active = True
            admin.is_superuser = True
            admin.is_admin = True
            admin.save()
        else:
            print("Admin accounts can only be initialized if no Accounts exist")
            