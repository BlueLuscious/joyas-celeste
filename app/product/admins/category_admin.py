from django.contrib import admin
from product.models.category_model import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):

    """ Admin for CategoryModel. """

    list_display = (
        "name",
        "get_subcategories",
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
    )

    def get_subcategories(self, obj: CategoryModel) -> str:

        """
        Get all subcategories from a CategoryModel Instance.
        Concatenate them in a string.

        Args:
            obj (CategoryModel): CategoryModel Instance.
        """

        return ", ".join([subcategory.name for subcategory in obj.subcategories.all()])
    get_subcategories.short_description = "Subcategories"
