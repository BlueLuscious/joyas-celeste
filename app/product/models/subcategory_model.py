from django.db import models
from django.utils.text import slugify
from typing import TYPE_CHECKING
from uuid import uuid4
if TYPE_CHECKING:
    from django.db.models import QuerySet
    from product.models.category_model import CategoryModel


class SubcategoryModel(models.Model):

    """
    Subcategory Model.

    Fields:
        uuid (UUID): Unique Universal Identifier.
        name (str): Subcategory name.
        slug (str): Subcategory name slugify.
        description (str): A description.
        created_at (datetime): Creation date.
        updated_at (datetime): Update date.

    Related Fields:
        categories (QuerySet[CategoryModel]): CategoryModel Instances.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, editable=False, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    categories: "QuerySet[CategoryModel]"


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Subcategory name.
        """

        return self.name


    def save(self, *args, **kwargs) -> None:

        """
        Overwrite save method.

        Actions:
            - Create slug.
        """
                
        if not self.slug:
            slug = slugify(self.name)
            if SubcategoryModel.objects.filter(slug=slug).exists():
                unique_id = str(self.uuid)[:8]
                slug = f"{slug}-{unique_id}"
            self.slug = slug
        super(SubcategoryModel, self).save(*args, **kwargs)
        
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "slug"], name="subcategory_name_slug")
        ]
