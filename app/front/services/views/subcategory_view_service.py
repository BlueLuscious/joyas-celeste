import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.models.subcategory_model import SubcategoryModel
from front.services.product_service import ProductService

logger = logging.getLogger(__name__)


class SubcategoryViewService():
    
    @staticmethod
    def get_context(name: str, sub_name: str, page: int) -> dict:

        """
        Get context for SubcategoryView.

        Get conxtext by name and sub_name, and page for paginate products.

        Args:
            name (str): Category name.
            sub_name (str): Subcategory name.
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
        subcategory = SubcategoryModel.objects.get(slug=sub_name.lower())
        products_by_subcategory = product_service.filter_products_by_stock().filter(
            category=category, subcategory=subcategory
        )
        pagination = product_service.paginate_products(products_by_subcategory, page, 12)

        context = {
            "categories": categories,
            "category": category,
            "subcategory": subcategory,
            "products": pagination.get("products_page"),
            "page_numbers": pagination.get("page_numbers"),
            "dollar_blue": dollar_blue_ask,
        }

        logger.info(f"subcategory_view context: {context}")
        return context
