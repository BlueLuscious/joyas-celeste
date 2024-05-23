import logging
from front.models.product_model import ProductModel
from front.models.category_model import CategoryModel

logger = logging.getLogger(__name__)


class IndexService():
    
    @staticmethod
    def get_context():
        products = ProductModel.objects.all()
        categories = CategoryModel.objects.all()

        context = {
            "products": products,
            "categories": categories,
        }
        logger.info(f"index context: {context}")

        return context
