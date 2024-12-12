import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.services.product_service import ProductService
from front.utils.context import Context

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

        product_service = ProductService(ProductModel.objects.all())

        categories = CategoryModel.objects.all()
        products = product_service.filter_products_by_stock()

        cripto_ya_service = CriptoYaService()
        dollar_quotes: dict = cripto_ya_service.get_dollar_quotes()
        dollar_blue_ask: float = dollar_quotes.get("blue").get("ask")

        context = Context(
            categories=categories,
            products=products.order_by("-created_at")[:12],
            dollar_blue=dollar_blue_ask,
        )

        logger.info(f"index_view context: {context.as_dict}")
        return context.as_dict
    