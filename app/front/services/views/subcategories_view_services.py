import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.models.subcategory_model import SubcategoryModel

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

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        context = {
            "categories": categories,
            "subcategories": subcategories,
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"subcategories_view context: {context}")
        return context
