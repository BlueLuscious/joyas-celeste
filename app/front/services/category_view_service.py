import logging
from django.template import Template, loader
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.services.product_service import ProductService

logger = logging.getLogger(__name__)


class CategoryViewService():
    
    @staticmethod
    def get_context(name: str, page: int) -> dict:

        """
        Get context by name: --> (CategoryView)

        If name is None, get context for /categories/ else get context for /categories/<str:name>/.

        Args:
            name (str): Category name.

        Returns:
            dict: Dictionary containing context data. (categories and products)
        """

        categories = CategoryModel.objects.all()
        product_service = ProductService()

        if name is None:
            products = product_service.get_random_products_for_each_category(categories, 10)

            context = {
                "categories": categories,
                "products": products,
            }

        else:
            category = CategoryModel.objects.get(name=name.capitalize())
            products_by_category = ProductModel.objects.filter(category=category)
            pagination = product_service.paginate_products(products_by_category, page, 12)

            context = {
                "categories": categories,
                "category": category,
                "products": pagination.get("products_page"),
                "page_numbers": pagination.get("page_numbers"),
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
        """

        if name is None:
            template = loader.get_template("pages/categories.html")
        else:
            template = loader.get_template("pages/category.html")

        logger.info(f"get template: {template.template.name}")
        return template
