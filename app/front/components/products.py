import logging
from django.core.paginator import Page
from django.db.models import QuerySet
from django_unicorn.components import UnicornView
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.models.subcategory_model import SubcategoryModel
from front.services.models.filters.product_filter_service import ProductFilterService
from front.services.models.orders.product_order_service import ProductOrderService
from front.services.page_service import PageService
from front.services.product_service import ProductService

logger = logging.getLogger(__name__)


class ProductsView(UnicornView):

    """
    Unicorn Component for Products. 

    **Bound Properties**:
        **products (QuerySet[ProductModel])**: Product Instances.
        **page_data (dict)**: Page Data.
        **page_numbers (list)**: Pagination controls range.

        **selected_category (str)**: Selected category.
        **selected_subcategory (str)**: Selected subcategory.
        **search_text (str)**: Search text.
    """

    products: QuerySet[ProductModel] = ProductModel.objects.none()
    page_data: dict = {}
    page_numbers: list = []

    selected_category: str = ""
    selected_subcategory: str = ""
    search_text: str = ""

    def __init__(self, *args, **kwargs) -> None:

        """ ProductsView Initializer. """

        super().__init__(*args, **kwargs)
        PRODUCTS: QuerySet[ProductModel] = ProductModel.objects.all()
        self.products_with_stock = ProductService(PRODUCTS).filter_products_by_stock()
        self.category: CategoryModel = kwargs.get("category")
        self.subcategory: SubcategoryModel = kwargs.get("subcategory")
        if self.category:
            self.selected_category = str(self.category.uuid)
        if self.subcategory:
            self.selected_subcategory = str(self.subcategory.uuid)
        self.update_products()


    def set_page(self, page_number: int = 1) -> None:
        
        """ 
        Set page from pagination controls reactively.
        
        Args:
            page_number (int): Current page number, default `1`.
        """

        self.update_products(page_number)

    
    def set_category(self, category_id: str = "") -> None:

        """
        Set category filter.

        Args:
            category_id (str): Category UUID.
        """

        self.selected_category = category_id
        self.update_products()


    def set_subcategory(self, subcategory_id: str = "") -> None:

        """
        Set subcategory filter.

        Args:
            subcategory_id (str): Subcategory UUID.
        """

        self.selected_subcategory = subcategory_id
        self.update_products()


    def set_search_text(self, text: str = "") -> None:
        
        """
        Set search engine filter.

        Args:
            search_text (str): Anything.
        """
        
        self.search_text = text
        self.update_products()


    def update_products(self, page_number: int = 1) -> None:
        
        """
        Update products, filter, order, etc. reactively.
        
        Args:
            page_number (int): Current page number, default `1`.
        """

        order_service = ProductOrderService(self.products_with_stock)
        self.products_with_stock = order_service.apply_orders()

        filter_service = ProductFilterService(self.products_with_stock)
        self.products_with_stock = filter_service.apply_filters(
            self.selected_category, self.selected_subcategory, self.search_text
        )

        self.get_paginated_products(page_number)


    def get_paginated_products(self, page_number: int = 1) -> None:

        """
        Obtain the paginated products reactively.

        Args:
            page_number (int): Current page number, default `1`.
        """

        pagination = ProductService(self.products_with_stock).paginate_products()
        page: Page = pagination.get_page(page_number)
        self.products = page.object_list
        page_service = PageService(page)
        self.page_data = page_service.page_data_as_dict(pagination)
        self.page_numbers = page_service.get_pagination_controls_range(pagination.num_pages, 5)
        