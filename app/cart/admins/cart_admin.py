from django.contrib import admin
from cart.models.cart_model import CartModel


@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):

    """ Admin for CartModel. """

    list_display = (
        "uuid",
        "user",
    )
    ordering = (
        "-created_at",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__username",
        "user__uuid",
        "items__product__name",
        "items__product__slug",
        "items__product__uuid",
        "items__product__category__name",
        "items__product__category__slug",
        "items__product__category__uuid",
        "items__product__subcategory__name",
        "items__product__subcategory__slug",
        "items__product__subcategory__uuid",
        "items__key",
        "items__size",
        "uuid",
    )
    # list_filter = ()
