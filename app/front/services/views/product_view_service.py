import logging
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class ProductViewService:

    """ Service for product view. """

    def __init__(self, name: str) -> None:

        """
        ProductViewService Initializer.

        Args:
            name (str): Product name or slug.
        """

        self.name = name

    
    def get_context(self) -> dict:

        """
        Get ProductModel by slug (name).

        Returns:
            dict: Dictionary containing a specific product.
        """

        product = ProductModel.objects.get(slug=self.name.lower())
        context = dict(product=product)

        logger.info(f"product_view context: {context}")
        return context
    