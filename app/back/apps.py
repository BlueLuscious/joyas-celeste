from django.apps import AppConfig


class BackConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "back"

    def ready(self) -> None:
        
        from .admins import (
            client_admin,
        )

        from .models import (
            client_model,
        )
