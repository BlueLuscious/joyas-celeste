from django.contrib import admin
from front.models.product_model import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "created_at", "id", )
    ordering = ("-created_at", )
    search_fields = ("id", "name", "category__uuid", "category__name", )
