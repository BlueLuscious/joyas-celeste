import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views import View
from front.services.views.subcategory_view_service import SubcategoryViewService
from typing import Optional

subcategory_view_service = SubcategoryViewService()
logger = logging.getLogger(__name__)


class SubcategoryView(View):
    def get(self, request: HttpRequest, name: Optional[str] = None, sub_name: Optional[str] = None, page: int = 1) -> HttpResponse:
        page = request.GET.get("page")
        
        template = subcategory_view_service.get_template(name)
        context = subcategory_view_service.get_context(name, sub_name, page)

        return HttpResponse(template.render(context, request))
