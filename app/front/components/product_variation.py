from typing import List
from django_unicorn.components import UnicornView


class ProductVariationView(UnicornView):
    product_stock: int

    def __init__(self, component_args: List | None = None, **kwargs):
        super().__init__(component_args, **kwargs)

        default_size = self.product.variations.filter(stock__gt=0).first()
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
