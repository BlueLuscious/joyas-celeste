import logging
from django_unicorn.components import UnicornView
from django.db.models import QuerySet
from product.models.product_model import ProductModel
from product.models.product_variation_model import ProductVariationModel

logger = logging.getLogger(__name__)


class ProductVariationView(UnicornView):

    """ 
    Unicorn Component for Product Variation. 

    **Bound Properties**:
        **variations: QuerySet[ProductVariationModel]**: Product Variation Instances.
        **product_stock: int**: Stock quantity of product variation.
    """
    
    variations: QuerySet[ProductVariationModel]
    product_stock: int = 0

    def __init__(self, *args, **kwargs) -> None:

        """ ProductVariationView Initializer. """

        super().__init__(*args, **kwargs)
        self.product: ProductModel
        self.variations = self.product.variations.filter(stock__gt=0).order_by("measure__size")

        if self.variations:
            default_size = self.variations.first()
            self.get_stock(default_size.measure.size)


    def get_stock(self, size: int) -> None:

        """
        Obtain the stock quantity of a product variation by size.

        Update `product_stock` reactively.

        Args:
            size (int): Product size.
        """

        variation = self.product.variations.filter(measure__size=size).first() # Bug: Sometimes get None
        self.product_stock = variation.stock if variation else 0
        logger.info(f"Product variation: {variation} | Variation stock: {self.product_stock}")
        