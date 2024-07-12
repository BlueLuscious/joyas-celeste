import logging
from back.services.cripto_ya_service import CriptoYaService
from django.template import Template, loader
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.models.subcategory_model import SubcategoryModel
from front.services.product_service import ProductService

logger = logging.getLogger(__name__)


class SubcategoryViewService():
    
    @staticmethod
    def get_context(name: str, sub_name: str, page: int) -> dict:

        """
        Get context by name: --> (SubcategoryView)

        If name is None, get context for /subcategories/ else 
        get context for /category/<str:name>/subcategory/<str:sub_name>/.

        Args:
            name (str): Category name.
            sub_name (str): Subcategory name.

        Returns:
            dict: Dictionary containing context data. 
            - categories and products
            - dollar quotation
        """

        categories = CategoryModel.objects.all()
        subcategories = SubcategoryModel.objects.all()
        product_service = ProductService()

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        if name is None:
            products = product_service.get_random_products_for_each_subcategory(subcategories, 10)

            context = {
                "categories": categories,
                "subcategories": subcategories,
                "products": products,
                "dollar_blue": dollar_blue_ask,
            }

        else:
            category = CategoryModel.objects.get(slug=name.lower())
            subcategory = SubcategoryModel.objects.get(slug=sub_name.lower())
            products_by_category = ProductModel.objects.filter(category=category, subcategory=subcategory)
            pagination = product_service.paginate_products(products_by_category, page, 12)

            context = {
                "categories": categories,
                "category": category,
                "subcategory": subcategory,
                "products": pagination.get("products_page"),
                "page_numbers": pagination.get("page_numbers"),
                "dollar_blue": dollar_blue_ask,
            }

        logger.info(f"categories_view context: {context}")
        return context
    
    
    @staticmethod
    def get_template(name: str) -> Template:
        
        """
        Get template by name: --> (SubcategoryView)

        If name is None, load /subtegories/ else 
        load /category/<str:name>/subcategory/<str:sub_name>/.

        Args:
            name (str): Subcategory name.

        Returns:
            Template: Django template.
        """

        if name is None:
            template = loader.get_template("pages/subcategories.html")
        else:
            template = loader.get_template("pages/subcategory.html")

        logger.info(f"get template: {template.template.name}")
        return template
