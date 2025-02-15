from typing import TYPE_CHECKING
from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from product.models.subcategory_model import SubcategoryModel
if TYPE_CHECKING:
    from django.db.models import QuerySet
    from product.models.product_model import ProductModel


class CategoryModel(models.Model):

    """ 
    Category Model.
    
    Fields:
        uuid (UUID): Unique Universal Identifier.
        name (str): Category name.
        slug (str): Category name slugify.
        subcategories (QuerySet[ProductModel]): SubcategoryModel Instances.
        description (str): A description.
        created_at (datetime): Creation date.
        updated_at (datetime): Update date.

    Related Fields:
        productmodel_set (QuerySet[ProductModel]): ProductModel Instances.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, editable=False, blank=True)
    subcategories: "QuerySet[SubcategoryModel]" = models.ManyToManyField(
        SubcategoryModel, related_name="categories"
    )
    description = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    productmodel_set: "QuerySet[ProductModel]"


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Category name.
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
            if CategoryModel.objects.filter(slug=slug).exists():
                unique_id = str(self.uuid)[:8]
                slug = f"{slug}-{unique_id}"
            self.slug = slug
        super(CategoryModel, self).save(*args, **kwargs)
        

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "slug"], name="category_name_slug")
        ]
