import logging
import random
from django.template import loader
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class CategoryService():
    
    @staticmethod
    def get_context(name):
        categories = CategoryModel.objects.all()

        if name is None:
            products_random_by_category = {
                category: random.sample(
                    list(ProductModel.objects.filter(category=category)), 
                    min(len(ProductModel.objects.filter(category=category)), 10)
                ) for category in categories
            }

            context = {
                "categories": categories,
                "products": products_random_by_category,
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
    
    @staticmethod
    def get_template(name):

        if name is None:
            template = loader.get_template("pages/categories.html")
        else:
            template = loader.get_template("pages/category.html")

        logger.info(f"get template: {template.template.name}")

        return template
