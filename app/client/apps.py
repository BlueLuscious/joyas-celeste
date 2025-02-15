from django.apps import AppConfig


class ClientConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "client"
    verbose_name = "Gestion de Usuarios"

    def ready(self) -> None:
        
        from .admins import (
            client_admin,
        )

        from .models import (
            client_model,
        )
        