from django.db.models import QuerySet
from product.models.product_model import ProductModel
from product.services.models.base_product_service import BaseProductService


class ProductOrderService(BaseProductService):

    """ Service to order ProductModel queryset. """

    def __init__(self, queryset: QuerySet[ProductModel]) -> None:
        super().__init__(queryset)
        self.order_list = []


    def order_by_criteria(self, criteria: str = "") -> str:

        """
        Add criteria to `order_list`.

        Args:
            criteria (str): Criteria to order.

        Returns:
            str: Criteria name.
        """

        if criteria != "":
            self.order_list.append(criteria)
        return criteria
        
    
    def apply_orders(
            self, name_order: str = "", price_order: str = "", creation_date_order: str = ""
        ) -> QuerySet[ProductModel]:

        """
        Apply the corresponding orders.

        Args:
            name_order (str): Name order.
            price_order (str): Price order.
            creation_date_order (str): Creation date order.

        Returns:
            queryset (QuerySet[ProductModel]): ProductModel Instances.
        """

        self.order_by_criteria(price_order)
        self.order_by_criteria(name_order)
        self.order_by_criteria(creation_date_order)
        return self.queryset.order_by(*self.order_list)
    