import logging
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class IndexViewService():
    
    @staticmethod
    def get_context() -> dict:

        """
        Get context: --> (IndexView)

        Returns:
            dict: Dictionary containing context data. (categories and products)
        """

        categories = CategoryModel.objects.all()
        products = ProductModel.objects.all()
        # .exclude(stock=0)

        context = {
            "categories": categories,
            "products": products,
        }

        logger.info(f"index_view context: {context}")

        return context
