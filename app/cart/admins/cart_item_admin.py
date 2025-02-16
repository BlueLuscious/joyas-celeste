from django.contrib import admin
from cart.models.cart_item_model import CartItemModel


@admin.register(CartItemModel)
class CartItemAdmin(admin.ModelAdmin):

    """ Admin for CartItemModel. """

    list_display = (
        "key",
        "cart",
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
        "cart__user__first_name",
        "cart__user__last_name",
        "cart__user__username",
        "cart__user__uuid",
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
    )
    list_filter = (
        "size",
        "product__category__name",
        "product__subcategory__name",
    )
