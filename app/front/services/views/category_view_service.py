import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.utils.context import Context

logger = logging.getLogger(__name__)


class CategoryViewService():
    
    @staticmethod
    def get_context(name: str) -> dict:

        """
        Get context for CategoryView.

        Get conxtext by name, and page for paginate products.

        Args:
            name (str): Category name.

        Returns:
            dict: Dictionary containing context data. 
            - categories, dollar.
        """

        categories = CategoryModel.objects.all()

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        category = CategoryModel.objects.get(slug=name.lower())

        context = Context(
            categories=categories,
            category=category,
            dollar_blue=dollar_blue_ask,
        )

        logger.info(f"category_view context: {context.as_dict}")
        return context.as_dict
