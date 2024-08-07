from typing import List
from django_unicorn.components import UnicornView
from front.models.product_variation_model import ProductVariationModel


class ProductVariationView(UnicornView):
    variations: ProductVariationModel
    product_stock: int

    def __init__(self, component_args: List | None = None, **kwargs):
        super().__init__(component_args, **kwargs)

        self.variations = self.product.variations.filter(stock__gt=0).order_by("stock")
        default_size = self.variations.first()
        if default_size:
            default_size = default_size.measure.size
            self.update_stock(default_size)
        else:
            self.product_stock = 0


    def update_stock(self, size: str) -> None:
        variation = self.product.variations.filter(measure__size=size).first()
        if variation:
            self.product_stock = variation.stock
        else:
            self.product_stock = 0
