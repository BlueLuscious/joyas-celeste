import logging
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class CategoryService():
    
    @staticmethod
    def get_context(name):
        if name is None:
            categories = CategoryModel.objects.all()
            products = ProductModel.objects.all()

            context = {
                "categories": categories,
                "products": products,
            }
        else:
            category = CategoryModel.objects.get(name=name.capitalize())
            products = ProductModel.objects.filter(category=category)

            context = {
                "category": category,
                "products": products,
            }

        logger.info(f"categories_view context: {context}")

        return context
