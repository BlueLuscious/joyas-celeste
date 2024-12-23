from django.contrib import admin
from front.models.subcategory_model import SubcategoryModel


@admin.register(SubcategoryModel)
class SubcategoryAdmin(admin.ModelAdmin):

    """ Admin for SubcategoryModel. """

    list_display = (
        "name",
        "get_categories",
        "slug",
        "uuid",
        "created_at",
        "updated_at",
    )
    ordering = (
        "-created_at",
    )
    search_fields = (
        "uuid",
        "name",
        "slug",
        "categories__uuid",
        "categories__name",
    )
    list_filter = (
        "categories__name",
    )

    def get_categories(self, obj: SubcategoryModel) -> str:
        
        """
        Get all categories from a SubcategoryModel Instance.
        Concatenate them in a string.

        Args:
            obj (SubcategoryModel): SubcategoryModel Instance.
        """

        return ", ".join([categories.name for categories in obj.categories.all()])
    get_categories.short_description = "Categories"
