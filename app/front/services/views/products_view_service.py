import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.services.product_service import ProductService

logger = logging.getLogger(__name__)


class ProductsViewService():
    
    @staticmethod
    def get_context(page: int) -> dict:

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
        product_service = ProductService()
        products = product_service.filter_products_by_stock()

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        pagination = product_service.paginate_products(products, page, 24)

        context = {
            "categories": categories,
            "products": pagination.get("products_page"),
            "page_numbers": pagination.get("page_numbers"),
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"products_view context: {context}")
        return context
