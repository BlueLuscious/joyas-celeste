import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel

logger = logging.getLogger(__name__)


class CategoriesViewService():

    @staticmethod
    def get_context() -> dict:

        """
        Get context for CategoriesView.

        Returns:
            dict: Dictionary containing context data.
            - categories, products, dollar.
        """
            
        categories = CategoryModel.objects.all()

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        context = {
            "categories": categories,
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"categories_view context: {context}")
        return context
