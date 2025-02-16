from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "order"
    verbose_name = "Gestion de Ordenes/Ventas"

    def ready(self) -> None:
        
        from .admins import (
            order_item_admin,
            order_admin,
        )

        from .models import (
            order_item_model,
            order_model,
        )
        