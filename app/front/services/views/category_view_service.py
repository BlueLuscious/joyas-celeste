import logging
from front.models.category_model import CategoryModel

logger = logging.getLogger(__name__)


class CategoryViewService:

    """ Service for category view. """

    def __init__(self, name: str) -> None:
        
        """ 
        CategoryViewService Initializer.
        
        Args:
            name (str): Category name or slug.
        """
        
        self.name = name
    

    def get_context(self) -> dict:

        """
        Get CategoryModel by slug (name).

        Returns:
            dict: Dictionary containing a CategoryModel Instance. 
        """

        category = CategoryModel.objects.get(slug=self.name.lower())
        context = dict(category=category)

        logger.info(f"category_view context: {context}")
        return context
    