from typing import TYPE_CHECKING
from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from product.models.category_model import CategoryModel
from product.models.subcategory_model import SubcategoryModel
if TYPE_CHECKING:
    from django.db.models import QuerySet
    from cart.models.cart_item_model import CartItemModel
    from product.models.product_variation_model import ProductVariationModel


class ProductModel(models.Model):

    """ 
    Product Model.

    Fields:
        uuid (UUID): Unique Universal Identifier.
        name (str): Product name.
        slug (str): Product name slugify.
        category (CategoryModel): CategoryModel Instance.
        subcatecory (SubcategoryModel): SubcategoryModel Instance.
        price (Decimal): Product price.
        image (ImageFieldFile): Illustraive image
        description (str): A description.
        created_at (datetime): Creation date.
        updated_at (datetime): Update date.

    Related Fields:
        cart_item (CartItemModel): CartItemModel Instance.
        variations (ProductVariationModel): ProductVariationModel Instances.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, editable=False, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    subcategory = models.ForeignKey(SubcategoryModel, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to="products", default=None, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cart_item: "CartItemModel"
    variations: "QuerySet[ProductVariationModel]"


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Product name.
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
            if ProductModel.objects.filter(slug=slug).exists():
                unique_id = str(self.uuid)[:8]
                slug = f"{slug}-{unique_id}"
            self.slug = slug
        super(ProductModel, self).save(*args, **kwargs)
        
        
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "slug"], name="product_name_slug")
        ]
