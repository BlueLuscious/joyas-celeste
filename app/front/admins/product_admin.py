from django.contrib import admin
from front.models.product_model import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "subcategory", "price", "stock", "slug", "uuid", "created_at", 
                    "updated_at", )
    ordering = ("-created_at", )
    search_fields = ("uuid", "name", "slug", "category__uuid", "category__name", "subcategory__uuid",
                    "subcategory__name", )
