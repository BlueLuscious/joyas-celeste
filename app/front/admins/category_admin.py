from django.contrib import admin
from front.models.category_model import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "get_subcategories", "slug", "uuid", "created_at", "updated_at", )
    ordering = ("-created_at", )
    search_fields = ("uuid", "name", "slug", )

    def get_subcategories(self, obj):
        return ", ".join([subcategory.name for subcategory in obj.subcategories.all()])
    get_subcategories.short_description = "Subcategories"
