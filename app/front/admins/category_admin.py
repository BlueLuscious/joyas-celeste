from django.contrib import admin
from front.models.category_model import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", )
    ordering = ("created_at", )
    search_fields = ("uuid", "name", )
