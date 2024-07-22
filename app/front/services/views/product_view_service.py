import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class ProductViewService():
    
    @staticmethod
    def get_context(name: str = None) -> dict:

        """
        Get context: --> (ProductView)

        Args:
            name (str): Product name (slug)

        Returns:
            dict: Dictionary containing context data.
            - categories
            - one specific product
            - dollar quotation
        """

        categories = CategoryModel.objects.all()
        product = ProductModel.objects.get(slug=name.lower())

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        context = {
            "categories": categories,
            "product": product,
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"product_view context: {context}")
        return context
