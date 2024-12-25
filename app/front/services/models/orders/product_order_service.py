from django.db.models import QuerySet
from front.models.product_model import ProductModel


class ProductOrderService:

    """ Service to order ProductModel queryset. """

    def __init__(self, queryset: QuerySet[ProductModel]) -> None:

        """
        ProductOrderService Initializer.

        Args:
            queryset (QuerySet[ProductModel]): ProductModel Instances.
        """

        self.queryset = queryset


    def order_by_creation_date(self, descending: bool = True) -> QuerySet[ProductModel]:

        """
        Order queryset by creation date. 

        Args:
            descending (bool): If it's `True` gets `-created_at` else `created_at`.

        Returns:
            QuerySet[ProductModel]: Ordered queryset by creation date.
        """
        
        return self.queryset.order_by("-created_at" if descending else "created_at")
    

    def apply_orders(self, descending: bool = True) -> QuerySet[ProductModel]:

        """
        Apply the corresponding orders.

        Args:
            queryset (QuerySet[ProductModel]): ProductModel Instances.
        """

        queryset = self.order_by_creation_date(descending)
        return queryset
    