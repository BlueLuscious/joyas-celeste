from django.contrib import admin
from product.models.product_variation_model import ProductVariationModel


@admin.register(ProductVariationModel)
class ProductVariationAdmin(admin.ModelAdmin):

    """ Admin for ProductVariationAModel. """

    list_display = (
        "product",
        "measure",
        "stock",
        "created_at",
        "updated_at",
    )
    ordering = (
        "-created_at",
    )
    search_fields = (
        "product__uuid",
        "product__name",
        "product__slug",
    )
