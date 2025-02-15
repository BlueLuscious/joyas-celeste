from django.db.models import Q, QuerySet
from product.models.product_model import ProductModel
from product.services.models.base_product_service import BaseProductService


class ProductFilterService(BaseProductService):

    """ Service to filter ProductModel queryset. """
    
    def filter_by_category(self, category_id: str) -> QuerySet[ProductModel]:

        """
        Filter queryset by category. 

        Args:
            category_id (str): Category UUID.

        Returns:
            QuerySet[ProductModel]: Filtered queryset by category.
        """

        if category_id != "":
            self.queryset = self.queryset.filter(category_id=category_id)
        return self.queryset


    def filter_by_subcategory(self, subcategory_id: str) -> QuerySet[ProductModel]:

        """
        Filter queryset by subcategory. 

        Args:
            subcategory_id (str): Subcategory UUID.

        Returns:
            QuerySet[ProductModel]: Filtered queryset by subcategory.
        """

        if subcategory_id != "":
            self.queryset = self.queryset.filter(subcategory_id=subcategory_id)
        return self.queryset


    def filter_by_search_text(self, search_text: str) -> QuerySet[ProductModel]:

        """
        Filter queryset by search text. 

        Args:
            search_text (str): Anything.

        Returns:
            QuerySet[ProductModel]: Filtered queryset by search text.
        """

        if search_text != "":
            self.queryset = self.queryset.filter(
                Q(name__icontains=search_text) | Q(description__icontains=search_text)
            )
        return self.queryset


    def apply_filters(
            self, category_id: str = "", subcategory_id: str = "", search_text: str = ""
        ) -> QuerySet[ProductModel]:

        """
        Apply the corresponding filters.

        Args:
            category_id (str): Category UUID.
            subcategory_id (str): Subcategory UUID.
            search_text (str): Anything.

        Returns:
            QuerySet[ProductModel]: Filtered queryset.
        """

        self.filter_by_category(category_id)
        self.filter_by_subcategory(subcategory_id)
        self.filter_by_search_text(search_text)
        return self.queryset
    