from django.db import models
from front.models.measure_model import MeasureModel
from front.models.product_model import ProductModel


class ProductVariationModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, related_name="variations")
    measure = models.ForeignKey(MeasureModel, on_delete=models.DO_NOTHING, related_name="variations")
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} - {self.measure.size}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["product", "measure"], name="product_measure")
        ]
