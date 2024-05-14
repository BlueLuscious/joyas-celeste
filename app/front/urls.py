from django.urls import path
from front.views.index_view import IndexView

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
]
