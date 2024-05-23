from django.contrib import admin
from front.models.product_model import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "created_at", )
    ordering = ("created_at", )
    search_fields = ("name", "category__name", )
