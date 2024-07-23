from django.urls import path
from front.views.cart.shopping_cart_view import ShoppingCartView
from front.views.categories_view import CategoriesView
from front.views.category_view import CategoryView
from front.views.index_view import IndexView
from front.views.product_view import ProductView
from front.views.products_view import ProductsView
from front.views.subcategories_view import SubcategoriesView
from front.views.subcategory_view import SubcategoryView


urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("categories/", CategoriesView.as_view(), name="categories"),
    path("category/<str:name>/", CategoryView.as_view(), name="category"),
    path("subcategories/", SubcategoriesView.as_view(), name="subcategories"),
    path("category/<str:name>/subcategory/<str:sub_name>/", SubcategoryView.as_view(), name="subcategory"),
    path("products/", ProductsView.as_view(), name="products"),
    path("product/<str:name>/", ProductView.as_view(), name="product"),
    path("cart/add/<uuid>/", ShoppingCartView.as_view(), name="add_product"),
    path("cart/remove/<uuid>/", ShoppingCartView.as_view(), name="remove_product"),
]
