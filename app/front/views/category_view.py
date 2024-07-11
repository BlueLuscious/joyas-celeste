import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views import View
from front.services.category_view_service import CategoryViewService
from typing import Optional

category_view_service = CategoryViewService()
logger = logging.getLogger(__name__)


class CategoryView(View):
    def get(self, request: HttpRequest, name: Optional[str] = None, page: int = 1) -> HttpResponse:
        page = request.GET.get("page")
        
        template = category_view_service.get_template(name)
        context = category_view_service.get_context(name, page)

        return HttpResponse(template.render(context, request))
