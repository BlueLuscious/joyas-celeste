from django.contrib import admin
from front.models.product_variation_model import ProductVariationModel


@admin.register(ProductVariationModel)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ("product", "measure", "stock", "created_at", "updated_at", )
    ordering = ("-created_at", )
    search_fields = ("product__uuid", "product__name", "product__slug", )
