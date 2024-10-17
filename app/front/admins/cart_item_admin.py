from django.contrib import admin
from front.models.cart_item_model import CartItemModel


@admin.register(CartItemModel)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "user",
        "product",
        "price",
        "size",
        "quantity",
    )
    ordering = (
        "-created_at",
    )
    search_fields = (
        "key",
        "product__name",
        "product__slug",
        "product__uuid",
        "product__category__name",
        "product__category__slug",
        "product__category__uuid",
        "product__subcategory__name",
        "product__subcategory__slug",
        "product__subcategory__uuid",
        "size",
        "user__first_name",
        "user__last_name",
        "user__username",
        "user__uuid",
    )
    list_filter = (
        "size",
        "product__category__name",
        "product__subcategory__name",
    )
