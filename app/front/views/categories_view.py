import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from front.services.views.categories_view_service import CategoriesViewService

logger = logging.getLogger(__name__)


class CategoriesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("pages/categories.html")

        categories_view_service = CategoriesViewService()
        context = categories_view_service.get_context()

        return HttpResponse(template.render(context, request))
