from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cart"
    verbose_name = "Gestion del Carro de Compras"

    def ready(self) -> None:
        
        from .admins import (
            cart_admin,
            cart_item_admin,
        )

        from .models import (
            cart_item_model,
            cart_model,
        )
