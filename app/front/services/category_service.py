import logging
import random
from django.template import Template, loader
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class CategoryService():
    
    @staticmethod
    def get_context(name: str) -> dict:

        """
        Get context by name: --> (CategoryView)

        If name is None, get context for /categories/ else get context for /categories/<str:name>.

        Args:
            name (str): Category name.

        Returns:
            dict: Dictionary containing context data. (categories and products)

        Logs:
            Show the context data.

        Example:
            context = category_service.get_template("Rings")
            
            context = category_service.get_template(None)
        """

        categories = CategoryModel.objects.all()

        if name is None:
            products_random_by_category = (lambda categories: [
                product for category in categories
                for product in random.sample(
                    list(ProductModel.objects.filter(category=category)),
                    min(len(ProductModel.objects.filter(category=category)), 10)
                )
            ])(categories)

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
    def get_template(name: str) -> Template:
        
        """
        Get template by name: --> (CategoryView)

        If name is None, load /categories/ else load /categories/<str:name>.

        Args:
            name (str): Category name.

        Returns:
            Template: Django template.

        Logs:
            Show the template name.

        Example:
            template = category_service.get_template("Rings")
            
            template = category_service.get_template(None)
        """

        if name is None:
            template = loader.get_template("pages/categories.html")
        else:
            template = loader.get_template("pages/category.html")

        logger.info(f"get template: {template.template.name}")
        return template
