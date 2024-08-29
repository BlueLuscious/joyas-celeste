from django.db import models
from front.models.product_model import ProductModel


class CartItemModel(models.Model):
    key = models.CharField(primary_key=True, max_length=128)
    product = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, related_name="cart_item")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    size = models.CharField(max_length=128)
    stock = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product.name
