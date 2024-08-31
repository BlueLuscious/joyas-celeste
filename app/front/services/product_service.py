import logging
from django.db.models import Exists, OuterRef
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from front.models.product_model import ProductModel
from front.models.product_variation_model import ProductVariationModel
from front.services.paginator_service import PaginatorService

logger = logging.getLogger(__name__)


class ProductService():

    @staticmethod
    def filter_products_by_stock() -> list[ProductModel]:

        """
        Get products with at least one variation having stock greater than 0.
        
        Returns:
            list: ProductModel instances with stock available.
        """
            
        variations_with_stock = ProductVariationModel.objects.filter(
            product=OuterRef("pk")
        ).exclude(stock=0)

        products = ProductModel.objects.annotate(
            has_stock=Exists(variations_with_stock)
        ).filter(has_stock=True)
        logger.info(f"products with stock: {products}")

        return products


    @staticmethod
    def paginate_products(products: QuerySet, page: int, quantity: int = 12) -> dict:

        """
        Paginate a list of products.

        Args:
            products (QuerySet): The queryset of products to paginate.
            page (int): The current page number.
            quantity (int): The number of products per page.

        Returns:
            dict: A dictionary containing the paginated products and page numbers for pagination.
        """

        pagination = Paginator(products, quantity)
        products_page = pagination.get_page(page)

        paginator_service = PaginatorService()
        page_numbers = paginator_service.calculate_page_numbers(products_page.number, pagination.num_pages, 5)

        data = {
            "products_page": products_page, 
            "page_numbers": page_numbers, 
        }
        logger.info(f"pagination data: {data}")

        return data
