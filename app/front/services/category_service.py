import logging
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class CategoryService():
    
    @staticmethod
    def get_context(name):
        categories = CategoryModel.objects.all()

        if name is None:
            products = ProductModel.objects.all()

            context = {
                "categories": categories,
                "products": products,
            }
        else:
            category = CategoryModel.objects.get(name=name.capitalize())
            products_by_category = ProductModel.objects.filter(category=category)

            context = {
                "categories": categories,
                "category": category,
                "products": products_by_category,
            }

        logger.info(f"categories_view context: {context}")

        return context
