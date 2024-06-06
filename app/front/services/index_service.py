import logging
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class IndexService():
    
    @staticmethod
    def get_context() -> dict:
        categories = CategoryModel.objects.all()
        products = ProductModel.objects.all()

        context = {
            "categories": categories,
            "products": products,
        }

        logger.info(f"index_view context: {context}")

        return context
