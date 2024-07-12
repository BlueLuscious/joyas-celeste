from django.contrib import admin
from front.models.subcategory_model import SubcategoryModel


@admin.register(SubcategoryModel)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "get_categories", "slug", "uuid", "created_at", "updated_at", )
    ordering = ("-created_at", )
    search_fields = ("uuid", "name", "slug", "categories__uuid", "categories__name", )
    list_filter = ("categories__name", )

    def get_categories(self, obj):
        return ", ".join([categories.name for categories in obj.categories.all()])
    get_categories.short_description = "Categories"
