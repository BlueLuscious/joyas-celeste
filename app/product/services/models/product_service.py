import logging
from django.db.models import Exists, OuterRef, QuerySet
from django.core.paginator import Paginator
from product.models.product_model import ProductModel
from product.models.product_variation_model import ProductVariationModel
from product.services.models.filters.product_filter_service import ProductFilterService
from product.services.models.orders.product_order_service import ProductOrderService

logger = logging.getLogger(__name__)


class ProductService(ProductFilterService, ProductOrderService):

    """
    Service for ProductModel queryset.

    Inheritance:
        ProductFilterService, ProductOrderService
    """

    def filter_products_by_stock(self) -> QuerySet[ProductModel]:

        """
        Get products with at least one variation having stock greater than 0.
        
        Returns:
            QuerySet[ProductModel]: ProductModel instances with stock available.
        """
            
        variations_with_stock = ProductVariationModel.objects.filter(
            product=OuterRef("pk")
        ).exclude(stock=0)

        self.queryset = self.queryset.annotate(
            has_stock=Exists(variations_with_stock)
        ).filter(has_stock=True)
        logger.info(f"Products with stock: {self.queryset}")

        return self.queryset


    def paginate_products(self, per_page: int = 12) -> Paginator:

        """
        Paginate a list of products.

        Args:
            per_page (int): The number of products per page.

        Returns:
            Paginator: A Paginator containing the paginated products.
        """

        pagination = Paginator(self.queryset, per_page)
        logger.info(f"Pagination data: {pagination}")
        return pagination
    