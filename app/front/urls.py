from django.urls import path
from front.views.index_view import IndexView
from front.views.category_view import CategoryView
from front.views.product_view import ProductView


urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("categories/", CategoryView.as_view(), name="categories"),
    path("categories/<str:name>/", CategoryView.as_view(), name="category"),
    path("product/<str:name>/", ProductView.as_view(), name="product"),
]
