from abc import ABC
from django.db.models import QuerySet
from product.models.product_model import ProductModel


class BaseProductService(ABC):

    """ Abstract Base Service for ProductModel related services. """

    def __init__(self, queryset: QuerySet[ProductModel]) -> None:

        """
        BaseProductService Initializer.

        Args:
            queryset (QuerySet[ProductModel]): ProductModel Instances.
        """
        
        self.queryset = queryset
        