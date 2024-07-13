import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.models.subcategory_model import SubcategoryModel
from front.services.product_service import ProductService

logger = logging.getLogger(__name__)


class SubcategoriesViewService():
    
    @staticmethod
    def get_context() -> dict:

        """
        Get context for SubcategoriesView

        Returns:
            dict: Dictionary containing context data. 
            - categories, products, dollar.
        """

        categories = CategoryModel.objects.all()
        subcategories = SubcategoryModel.objects.all()
        product_service = ProductService()

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        products = product_service.get_random_products_for_each_subcategory(subcategories, 10)

        context = {
            "categories": categories,
            "subcategories": subcategories,
            "products": products,
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"subcategories_view context: {context}")
        return context
