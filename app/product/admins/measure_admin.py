from django.contrib import admin
from product.models.measure_model import MeasureModel


@admin.register(MeasureModel)
class MeasureAdmin(admin.ModelAdmin):

    """ Admin for MeasureModel. """

    list_display = (
        "size",
        "milimeters",
        "uuid",
        "created_at",
        "updated_at",
    )
    ordering = (
        "-created_at",
    )
    search_fields = (
        "uuid",
        "size",
        "milimeters",
    )
