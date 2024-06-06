import logging
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class IndexService():
    
    @staticmethod
    def get_context() -> dict:

        """
        Get context: --> (IndexView)

        Returns:
            dict: Dictionary containing context data. (categories and products)

        Logs:
            Show the context data.

        Example:
            context = index_service.get_template("Rings")
            
            context = index_service.get_template(None)
        """

        categories = CategoryModel.objects.all()
        products = ProductModel.objects.all()

        context = {
            "categories": categories,
            "products": products,
        }

        logger.info(f"index_view context: {context}")

        return context
