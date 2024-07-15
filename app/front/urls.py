from django.urls import path
from front.views.index_view import IndexView
from front.views.categories_view import CategoriesView
from front.views.category_view import CategoryView
from front.views.product_view import ProductView
from front.views.subcategories_view import SubcategoriesView
from front.views.subcategory_view import SubcategoryView


urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("categories/", CategoriesView.as_view(), name="categories"),
    path("category/<str:name>/", CategoryView.as_view(), name="category"),
    path("subcategories/", SubcategoriesView.as_view(), name="subcategories"),
    path("category/<str:name>/subcategory/<str:sub_name>/", SubcategoryView.as_view(), name="subcategory"),
    path("product/<str:name>/", ProductView.as_view(), name="product"),
]
