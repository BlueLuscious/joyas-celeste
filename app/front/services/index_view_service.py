import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class IndexViewService():
    
    @staticmethod
    def get_context() -> dict:

        """
        Get context: --> (IndexView)

        Returns:
            dict: Dictionary containing context data.
            - categories and products
            - dollar quotation
        """

        categories = CategoryModel.objects.all()
        products = ProductModel.objects.all()
        # .exclude(stock=0)

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes()
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        context = {
            "categories": categories,
            "products": products,
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"index_view context: {context}")

        return context
