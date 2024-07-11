from django.contrib import admin
from front.models.product_model import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "created_at", "slug", "uuid", )
    ordering = ("-created_at", )
    search_fields = ("uuid", "name", "slug", "category__uuid", "category__name", )
