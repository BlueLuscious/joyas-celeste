import logging
from back.services.cripto_ya_service import CriptoYaService
from front.models.category_model import CategoryModel
from front.models.subcategory_model import SubcategoryModel
from front.utils.context import Context

logger = logging.getLogger(__name__)


class SubcategoryViewService():
    
    @staticmethod
    def get_context(name: str, sub_name: str) -> dict:

        """
        Get context for SubcategoryView.

        Get conxtext by name and sub_name, and page for paginate products.

        Args:
            name (str): Category name.
            sub_name (str): Subcategory name.

        Returns:
            dict: Dictionary containing context data. 
            - categories dollar.
        """

        categories = CategoryModel.objects.all()

        cripto_ya_service = CriptoYaService()
        dollar_quotes: dict = cripto_ya_service.get_dollar_quotes()
        dollar_blue_ask: float = dollar_quotes.get("blue").get("ask")

        category = CategoryModel.objects.get(slug=name.lower())
        subcategory = SubcategoryModel.objects.get(slug=sub_name.lower())

        context = Context(
            categories=categories,
            category=category,
            subcategory=subcategory,
            dollar_blue=dollar_blue_ask,
        )

        logger.info(f"subcategory_view context: {context.as_dict}")
        return context.as_dict
