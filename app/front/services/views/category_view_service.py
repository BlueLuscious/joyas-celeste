import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.services.product_service import ProductService

logger = logging.getLogger(__name__)


class CategoryViewService():
    
    @staticmethod
    def get_context(name: str, page: int) -> dict:

        """
        Get context for CategoryView.

        Get conxtext by name, and page for paginate products.

        Args:
            name (str): Category name.
            page (int): Page number.

        Returns:
            dict: Dictionary containing context data. 
            - categories, product pagination, dollar.
        """

        categories = CategoryModel.objects.all()
        product_service = ProductService()

        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes().get("data")
        dollar_blue_ask = dollar_quotes.get("blue").get("ask")

        category = CategoryModel.objects.get(slug=name.lower())
        products_by_category = product_service.filter_products_by_stock().filter(category=category)
        pagination = product_service.paginate_products(products_by_category, page, 12)

        context = {
            "categories": categories,
            "category": category,
            "products": pagination.get("products_page"),
            "page_numbers": pagination.get("page_numbers"),
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"category_view context: {context}")
        return context
