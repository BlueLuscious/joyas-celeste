from django.apps import AppConfig


class FrontConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "front"

    def ready(self) -> None:
        
        from .admins import (
            category_admin,
            product_admin,
            subcategory_admin,
        )

        from .models import (
            category_model,
            product_model,
            subcategory_model,
        )
