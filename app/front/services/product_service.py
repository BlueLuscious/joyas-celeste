import logging
from django.db.models import Exists, OuterRef
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from front.models.product_model import ProductModel
from front.models.product_variation_model import ProductVariationModel

logger = logging.getLogger(__name__)


class ProductService:

    def __init__(self, product: ProductModel | QuerySet[ProductModel]) -> None:
        self.product = product if isinstance(product, ProductModel) else None
        self.products = product if isinstance(product, QuerySet[ProductModel]) else None

    def filter_products_by_stock(self) -> QuerySet[ProductModel]:

        """
        Get products with at least one variation having stock greater than 0.
        
        Returns:
            QuerySet[ProductModel]: ProductModel instances with stock available.
        """
            
        variations_with_stock = ProductVariationModel.objects.filter(
            product=OuterRef("pk")
        ).exclude(stock=0)

        self.products = self.products.annotate(
            has_stock=Exists(variations_with_stock)
        ).filter(has_stock=True)
        logger.info(f"products with stock: {self.products}")

        return self.products


    def paginate_products(self, per_page: int = 12) -> Paginator:

        """
        Paginate a list of products.

        Args:
            per_page (int): The number of products per page.

        Returns:
            Paginator: A Paginator containing the paginated products.
        """

        pagination = Paginator(self.products, per_page)
        logger.info(f"pagination data: {pagination}")
        return pagination
    