import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.utils.context import Context

logger = logging.getLogger(__name__)


class ProductsViewService():
    
    @staticmethod
    def get_context() -> dict:

        """
        Get context: --> (ProductsView)

        Get conxtext, and page for paginate products.

        Args:
            page (int): Page naumber

        Returns:
            dict: Dictionary containing context data.
            - categories and products
            - dollar quotation
        """

        categories = CategoryModel.objects.all()

        cripto_ya_service = CriptoYaService()
        dollar_quotes: dict = cripto_ya_service.get_dollar_quotes()
        dollar_blue_ask: float = dollar_quotes.get("blue").get("ask")

        context = Context(
            categories=categories,
            dollar_blue=dollar_blue_ask,
        )

        logger.info(f"products_view context: {context.as_dict}")
        return context.as_dict
