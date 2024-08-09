import logging
import random
from django.db.models import Exists, OuterRef
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.models.product_variation_model import ProductVariationModel
from front.models.subcategory_model import SubcategoryModel
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

        return products


    @staticmethod
    def get_random_products_for_each_category(categories: CategoryModel, quantity: int = 10) -> list[ProductModel]:

        """
        Get a list of random products for each category.

        Args:
            categories CategoryModel: An iterable containing CategoryModel instances.
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
    def get_random_products_for_each_subcategory(subcategories: SubcategoryModel, quantity: int = 10) -> list[ProductModel]:

        """
        Get a list of random products for each subcategory.

        Args:
            subcategories SubcategoryModel: An iterable containing SubcategoryModel instances.
            quantity (int): The number of random products to retrieve for each subcategory.

        Returns:
            list: A list containing random ProductModel instances for each subcategory.
        """

        random_products_by_subcategory = (lambda subcategories: [
            product for subcategory in subcategories
            for product in random.sample(
                list(ProductModel.objects.filter(subcategory=subcategory)),
                min(len(ProductModel.objects.filter(subcategory=subcategory)), quantity)
            )
        ])(subcategories)

        logger.info(f"random products by subcategory: {random_products_by_subcategory}")
        return random_products_by_subcategory


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
