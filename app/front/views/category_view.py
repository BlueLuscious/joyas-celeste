import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from front.services.views.category_view_service import CategoryViewService

logger = logging.getLogger(__name__)


class CategoryView(View):
    def get(self, request: HttpRequest, name: str) -> HttpResponse:
        template = loader.get_template("pages/category.html")

        category_view_service = CategoryViewService()
        context = category_view_service.get_context(name)

        return HttpResponse(template.render(context, request))
