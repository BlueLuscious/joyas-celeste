import logging
import random
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.services.paginator_service import PaginatorService
from typing import Iterable

logger = logging.getLogger(__name__)


class ProductService():

    @staticmethod
    def get_random_products_by_category(categories: Iterable[CategoryModel], quantity: int = 10) -> list[ProductModel]:

        """
        Get a list of random products for each category.

        Args:
            categories (Iterable[CategoryModel]): An iterable containing CategoryModel instances.
            quantity (int): The number of random products to retrieve for each category.

        Returns:
            list: A list containing random ProductModel instances for each category.
        """

        random_products_by_category = (lambda categories: [
            product for category in categories
            for product in random.sample(
                list(ProductModel.objects.filter(category=category)),
                min(len(ProductModel.objects.filter(category=category)), quantity)
            )
        ])(categories)

        logger.info(f"random products by category: {random_products_by_category}")
        return random_products_by_category


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
