import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from front.services.views.subcategory_view_service import SubcategoryViewService

logger = logging.getLogger(__name__)


class SubcategoryView(View):
    def get(self, request: HttpRequest, name: str, sub_name: str, page: int = 1) -> HttpResponse:
        template = loader.get_template("pages/subcategory.html")
        
        page = request.GET.get("page")
        subcategory_view_service = SubcategoryViewService()
        context = subcategory_view_service.get_context(name, sub_name, page)

        return HttpResponse(template.render(context, request))
