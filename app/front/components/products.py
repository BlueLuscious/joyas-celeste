import logging
from django.core.paginator import Page
from django.db.models import QuerySet
from django_unicorn.components import UnicornView
from front.services.page_service import PageService
from product.models.category_model import CategoryModel
from product.models.product_model import ProductModel
from product.models.subcategory_model import SubcategoryModel
from product.services.models.product_service import ProductService

logger = logging.getLogger(__name__)


class ProductsView(UnicornView):

    """
    Unicorn Component for Products. 

    **Bound Properties**:
        **products (QuerySet[ProductModel])**: Product Instances.
        **page_data (dict)**: Page Data.
        **page_numbers (list)**: Pagination controls range.

        **selected_category_filter (str)**: Category filter.
        **selected_subcategory_filter (str)**: Subcategory filter.
        **selected_search_text (str)**: Search text filter.

        **selected_creation_date_order (str)**: = Creation date order"
        **selected_price_order (str)**: = Price order.
        **selected_name_order (str)**: = Name order.
    """

    products: QuerySet[ProductModel] = ProductModel.objects.none()
    page_data: dict = {}
    page_numbers: list = []

    # Filters
    selected_category_filter: str = ""
    selected_subcategory_filter: str = ""
    selected_search_text: str = ""

    # Orders
    selected_creation_date_order: str = f"-{ProductModel.created_at.field.name}"
    selected_price_order: str = ""
    selected_name_order: str = ""

    def __init__(self, *args, **kwargs) -> None:

        """ ProductsView Initializer. """

        super().__init__(*args, **kwargs)
        PRODUCTS: QuerySet[ProductModel] = ProductModel.objects.all()
        self.product_service = ProductService
        self.products_with_stock = self.product_service(PRODUCTS).filter_products_by_stock()
        self.category: CategoryModel = kwargs.get("category")
        self.subcategory: SubcategoryModel = kwargs.get("subcategory")
        self.selected_category_filter = str(self.category.uuid) if self.category else self.selected_category_filter
        self.selected_subcategory_filter = str(self.subcategory.uuid) if self.subcategory else self.selected_subcategory_filter
        self.update_products()


    def set_page(self, page_number: int = 1) -> None:
        
        """ 
        Set page from pagination controls reactively.
        
        Args:
            page_number (int): Current page number, default `1`.
        """

        self.update_products(page_number)


    def set_selected_query(self, selected_criteria: str, criteria_query: str =  "") -> None:

        """
        Set selected filter, order, etc. reactively.

        Args:
            selected_criteria (str): Criteria name.
            criteria_query (str): Query value.
        """
        
        setattr(self, selected_criteria, criteria_query)
        self.update_products()


    def update_products(self, page_number: int = 1) -> None:
        
        """
        Update products, filter, order, etc. reactively.
        
        Args:
            page_number (int): Current page number, default `1`.
        """

        self.products_with_stock = self.product_service(self.products_with_stock).apply_orders(
            self.selected_name_order,
            self.selected_price_order,
            self.selected_creation_date_order
        )

        self.products_with_stock = self.product_service(self.products_with_stock).apply_filters(
            self.selected_category_filter,
            self.selected_subcategory_filter,
            self.selected_search_text
        )

        self.get_paginated_products(page_number)


    def get_paginated_products(self, page_number: int = 1) -> None:

        """
        Obtain the paginated products reactively.

        Args:
            page_number (int): Current page number, default `1`.
        """

        pagination = self.product_service(self.products_with_stock).paginate_products()
        page: Page = pagination.get_page(page_number)
        self.products = page.object_list
        page_service = PageService(page)
        self.page_data = page_service.page_data_as_dict(pagination)
        self.page_numbers = page_service.get_pagination_controls_range(pagination.num_pages, 5)
        