from django.urls import path
from front.views.index_view import IndexView

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    # path("ring/", IndexView.as_view(), name="ring"),
    # path("earring", IndexView.as_view(), name="earring"),
    # path("necklace/", IndexView.as_view(), name="necklace"),
    # path("bracelet/", IndexView.as_view(), name="bracelet"),
]
