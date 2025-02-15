import logging
from django.core.paginator import Page
from django.db.models import QuerySet
from django_unicorn.components import UnicornView
from front.services.pagination_service import PaginatorService
from product.models.category_model import CategoryModel
from product.models.product_model import ProductModel
from product.models.subcategory_model import SubcategoryModel
from product.services.models.product_service import ProductService

logger = logging.getLogger(__name__)


class ProductsView(UnicornView):

    """
    Unicorn Component for Products. 

    **Bound Properties**:
        **products (QuerySet[ProductModel])**: ProductModel Instances.
        **page_data (dict)**: Page Data.
        **page_numbers (list)**: Pagination controls range.

        **selected_category (CategoryModel)**: CategoryModel Instance.
        **selected_subcategory (SubcategoryModel)**: SubcategoryModel Instance.

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

    # Model Instances
    selected_category: CategoryModel | None = None
    selected_subcategory: SubcategoryModel | None = None

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
        self.product_service = ProductService
        self.products_with_stock = self.product_service(ProductModel.objects.all()).filter_products_by_stock()
        self.category: CategoryModel = kwargs.get("category")
        self.subcategory: SubcategoryModel = kwargs.get("subcategory")
        self.selected_category_filter = str(self.category.uuid) if self.category else self.selected_category_filter
        self.selected_subcategory_filter = str(self.subcategory.uuid) if self.subcategory else self.selected_subcategory_filter
        self.update_products()
        

    def update_products(self, page_number: int = 1) -> None:
        
        """
        Update products reactively.

        Actions:
            - Filter and order products.
            - Paginate products.
        
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

        pagination = self.product_service(self.products_with_stock).paginate_products()
        pagination_service = PaginatorService(pagination, page_number)
        self.products = pagination_service.get_object_list()
        self.page_data = pagination_service.page_data_as_dict()
        self.page_numbers = pagination_service.get_pagination_controls_range(5)


    def updated_selected_category_filter(self, value: str) -> None:

        """
        Trigger when `selected_category_filter` is updated.

        Args:
            value (str): `selected_category_filter` value.
        """

        self.selected_category = None if value == "" else CategoryModel.objects.get(pk=value)
        self.selected_subcategory = None if self.selected_subcategory_filter == "" else SubcategoryModel.objects.get(pk=self.selected_subcategory_filter)
    

    def updated_selected_subcategory_filter(self, value: str) -> None:

        """
        Trigger when `selected_subcategory_filter` is updated.

        Args:
            value (str): `selected_subcategory_filter` value.
        """

        self.selected_category = None if self.selected_category_filter == "" else CategoryModel.objects.get(pk=self.selected_category_filter)
        self.selected_subcategory = None if value == "" else SubcategoryModel.objects.get(pk=value)
        