from django.urls import path
from front.views.category_view import CategoryView
from front.views.checkout_view import CheckoutView
from front.views.index_view import IndexView
from front.views.product_view import ProductView
from front.views.products_view import ProductsView
from front.views.profile_view import ProfileView
from front.views.subcategory_view import SubcategoryView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("category/<str:name>/", CategoryView.as_view(), name="category"),
    path("category/<str:name>/subcategory/<str:sub_name>/", SubcategoryView.as_view(), name="subcategory"),
    path("products/", ProductsView.as_view(), name="products"),
    path("product/<str:name>/", ProductView.as_view(), name="product"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
]
