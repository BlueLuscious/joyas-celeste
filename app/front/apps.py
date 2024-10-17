from django.apps import AppConfig


class FrontConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "front"

    def ready(self) -> None:
        
        from .admins import (
            cart_item_admin,
            category_admin,
            measure_admin,
            product_admin,
            product_variation_admin,
            subcategory_admin,
        )

        from .models import (
            cart_item_model,
            category_model,
            measure_model,
            product_model,
            product_variation_model,
            subcategory_model,
        )
