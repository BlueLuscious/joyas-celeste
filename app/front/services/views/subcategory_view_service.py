import logging
from product.models.category_model import CategoryModel
from product.models.subcategory_model import SubcategoryModel

logger = logging.getLogger(__name__)


class SubcategoryViewService:

    """ Service for subcategory view. """

    def __init__(self, name: str, sub_name: str) -> None:

        """
        SubcategoryViewService Initializer.
        
        Args:
            name (str): Category name or slug.
            sub_name (str): Subcategory name or slug.
        """

        self.name = name
        self.sub_name = sub_name
    

    def get_context(self) -> dict:

        """
        Get CategoryModel by slug (name) and SubcategoryModel by slug (sub_name).

        Returns:
            dict: Dictionary containing a CategoryModel Instance and a Subcategory Instance.
        """

        category = CategoryModel.objects.get(slug=self.name.lower())
        subcategory = SubcategoryModel.objects.get(slug=self.sub_name.lower())
        context = dict(category=category, subcategory=subcategory)

        logger.info(f"subcategory_view context: {context}")
        return context
    