from django.db import models
from django.utils.text import slugify
from front.models.category_model import CategoryModel
from front.models.measure_model import MeasureModel
from front.models.subcategory_model import SubcategoryModel
from uuid import uuid4


class ProductModel(models.Model):
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

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs) -> None:
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
