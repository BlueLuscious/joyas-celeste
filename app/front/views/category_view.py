import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from front.services.views.category_view_service import CategoryViewService

logger = logging.getLogger(__name__)


class CategoryView(View):
    def get(self, request: HttpRequest, name: str, page: int = 1) -> HttpResponse:
        template = loader.get_template("pages/category.html")
        
        page = request.GET.get("page")
        category_view_service = CategoryViewService()
        context = category_view_service.get_context(name, page)

        return HttpResponse(template.render(context, request))
