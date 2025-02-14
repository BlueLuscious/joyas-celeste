from django.apps import AppConfig


class FrontConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "front"

    def ready(self) -> None:
        
        from .admins import (
            cart_item_admin,
        )

        from .models import (
            cart_item_model,
        )
