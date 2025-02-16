from django.contrib import admin
from order.models.order_model import OrderModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):

    """ Admin for OrderModel. """

    list_display = (
        "uuid",
        "user",
        "status",
        "paid",
        "created_at",
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
        "items__uuid",
        "items__size",
        "status",
        "uuid",
    )
    list_filter = (
        "status",
        "paid",
        "created_at",
    )
