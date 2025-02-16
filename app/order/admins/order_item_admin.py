from django.contrib import admin
from order.models.order_item_model import OrderItemModel


@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):

    """ Admin for OrderItemModel. """

    list_display = (
        "uuid",
        "order",
        "product",
        "price",
        "size",
        "quantity",
    )
    ordering = (
        "-created_at",
    )
    search_fields = (
        "order__user__first_name",
        "order__user__last_name",
        "order__user__username",
        "order__user__uuid",
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
        "uuid",
    )
    list_filter = (
        "size",
        "product__category__name",
        "product__subcategory__name",
    )
