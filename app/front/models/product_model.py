from django.db import models
from front.models.category_model import CategoryModel
from uuid import uuid4


class ProductModel(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products", default=None, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
