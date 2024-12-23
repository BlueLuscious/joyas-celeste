from django.core.paginator import Page
from django.db.models import QuerySet
from django_unicorn.components import UnicornView
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.models.subcategory_model import SubcategoryModel
from front.services.page_service import PageService
from front.services.product_service import ProductService


class ProductsView(UnicornView):

    """
    Unicorn Component for Products. 

    **Bound Properties**:
        **products (QuerySet[ProductModel])**: Product Instances.
        **page_data (dict)**: Page Data.
        **page_numbers (list)**: Total number of pages.
        **categories (QuerySet[CategoryModel])**: Category Instances.
        **subcategories (QuerySet[SubcategoryModel])**: Subcategory Instances.

        **selected_category (str)**: Selected category.
        **selected_subcategory (str)**: Selected subcategory.
        **search_text (str)**: Search text.
    """

    products: QuerySet[ProductModel] = ProductModel.objects.none()
    page_data: dict = {}
    page_numbers: list = []
    categories: QuerySet[CategoryModel] = CategoryModel.objects.all()
    subcategories: QuerySet[SubcategoryModel] = SubcategoryModel.objects.all()

    selected_category: str = ""
    selected_subcategory: str = ""
    search_text: str = ""

    def __init__(self, *args, **kwargs) -> None:

        """ ProductsView Initializer. """

        super().__init__(*args, **kwargs)
        self.products_with_stock: QuerySet[ProductModel] = ProductService(
            ProductModel.objects.all()
        ).filter_products_by_stock().order_by("-created_at")
        if kwargs.get("category"):
            self.products_with_stock = self.products_with_stock.filter(category=kwargs.get("category"))
        if kwargs.get("subcategory"):
            self.products_with_stock = self.products_with_stock.filter(subcategory=kwargs.get("subcategory"))
        self.get_paginated_products()

    def hydrate(self) -> None:
        self.categories = CategoryModel.objects.all()
        self.subcategories = SubcategoryModel.objects.all()

    def set_page(self, page_number: int = 1) -> None:
        
        """ Set page from pagination controls. """

        self.update_products(page_number)

    def get_paginated_products(self, page_number: int = 1) -> None:

        """ Obtain the paginated products reactively. """

        pagination = ProductService(self.products_with_stock).paginate_products(1) # setear en 12
        page: Page = pagination.get_page(page_number)
        self.products = page.object_list
        page_service = PageService(page)
        self.page_data = page_service.page_data_as_dict(pagination)
        self.page_numbers = page_service.get_pagination_controls_range(pagination.num_pages, 5)

    def update_products(self, page_number: int = 1) -> None:
        
        """ Update products, filter, order, etc. """

        queryset = self.products_with_stock

        if self.selected_category != "":
            queryset = queryset.filter(category_id=self.selected_category)
        if self.selected_subcategory != "":
            queryset = queryset.filter(subcategory_id=self.selected_subcategory)
        if self.search_text != "":
            queryset = queryset.filter(name__icontains=self.search_text)

        self.products_with_stock = queryset
        self.get_paginated_products(page_number)

    def filter_products(self) -> None:
        """  Filter products by criteria. """
        pass

    def order_products(self) -> None:
        """  Order products by criteria. """
        pass

    def set_category(self, category_id: str = "") -> None:
        """ Set category filter. """
        self.selected_category = category_id
        self.update_products()

    def set_subcategory(self, subcategory_id: str = "") -> None:
        """ Set subcategory filter. """
        self.selected_subcategory = subcategory_id
        self.update_products()

    def set_search_text(self, text: str = "") -> None:
        """ Set search engine filter. """
        self.search_text = text
        self.update_products()
        