import logging
from front.models.product_model import ProductModel
from front.services.product_service import ProductService

logger = logging.getLogger(__name__)


class IndexViewService:

    """ Service for index view. """

    def __init__(self) -> None:

        """ IndexViewService Initializer. """

        pass
    

    def get_context(self) -> dict:

        """
        Get context for index view.

        Returns:
            dict: Dictionary containing products queryset.
        """

        product_service = ProductService(ProductModel.objects.all())
        products = product_service.filter_products_by_stock()
        context = dict(products=products.order_by("-created_at")[:12])

        logger.info(f"index_view context: {context}")
        return context
    