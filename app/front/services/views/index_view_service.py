import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.services.product_service import ProductService

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

        product_service = ProductService()

        categories = CategoryModel.objects.all()
        products = product_service.filter_products_by_stock()

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        context = {
            "categories": categories,
            "products": products.order_by("-created_at")[:12],
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"index_view context: {context}")
        return context
